import logging
import re
import time

from bs4 import BeautifulSoup as BS
from pretty_utils.miscellaneous.files import read_json
from pretty_utils.miscellaneous.time_and_date import unix_to_strtime
from pretty_utils.type_functions.strings import text_between
from py_steam import exceptions
from py_steam.client import WebClient
from py_steam.guard import generate_one_time_code

from data import config
from data.models import Statuses, Settings
from functions.get_mafile_dict import get_mafile_dict
from utils.db_api.database import db, get_unchecked_accounts
from utils.miscellaneous.get_random_proxy import get_random_proxy
from utils.miscellaneous.print_to_log import print_to_log


def get_rank(client: WebClient) -> int:
    html = client.session.get(url=f'{client.steamid.profile_url}/gcpd/730')
    soup = BS(html.text, 'html.parser')
    elements = soup.find_all('div', class_='generic_kv_line')
    for element in elements:
        text = element.get_text(strip=True)
        if 'cs:go' in text.lower():
            return int(re.findall(r'\d+', text)[0])

    return 0


def check() -> None:
    try:
        print('\nChecking...')
        settings = Settings()
        mafiles = get_mafile_dict()
        unchecked_accounts = get_unchecked_accounts()
        total = len(unchecked_accounts)
        for i, account in enumerate(unchecked_accounts):
            try:
                client = WebClient(proxy=get_random_proxy())
                twofactor_code = ''
                if account.login in mafiles:
                    twofactor_code = generate_one_time_code(
                        shared_secret=read_json(mafiles[account.login]).get('shared_secret')
                    )

                client.login(username=account.login, password=account.password, twofactor_code=twofactor_code)
                account.status = Statuses.Checked
                account.rank = get_rank(client=client)
                text = f'Rank: {account.rank}'
                if settings.parse.last_online:
                    try:
                        profile = client.session.get(client.steamid.profile_url)
                        last_online = text_between(
                            text=profile.text, begin='<div class="profile_in_game_name">', end='</div>'
                        )
                        seconds_multiplier = 0
                        surcharge = 0
                        if 'day' in last_online:
                            seconds_multiplier = 86400

                        elif 'hr' in last_online:
                            seconds_multiplier = 3600
                            parts = last_online.split(',')
                            for part in parts:
                                if 'hr' in part:
                                    last_online = part

                                elif 'min' in part:
                                    parsed_value = re.sub('[^0-9]', '', part)
                                    if parsed_value:
                                        surcharge = int(parsed_value) * 60

                        elif 'min' in last_online:
                            seconds_multiplier = 60

                        parsed_value = re.sub('[^0-9]', '', last_online)
                        if parsed_value:
                            account.last_online = int(time.time()) - surcharge - int(parsed_value) * seconds_multiplier
                            text += f' | Last online: {unix_to_strtime(unix_time=account.last_online, format="%d.%m.%Y %H:%M")}'

                    except BaseException as e:
                        logging.exception('last_online')
                        text += f' | Last online: {e}'

                print_to_log(text=text, color=color, i=i, total=total, account=account)

            except exceptions.LoginIncorrect:
                account.status = Statuses.WrongCredentials
                print_to_log(text='Wrong credentials!', color=failed_color, i=i, total=total, account=account)

            except exceptions.CaptchaRequired:
                print_to_log(text='Captcha required!', color=failed_color, i=i, total=total, account=account)

            except exceptions.TwoFactorCodeRequired:
                print_to_log(
                    text='Invalid maFile or already used Steam Guard code!', color=failed_color, i=i, total=total,
                    account=account
                )

            except exceptions.TooManyLoginFailures:
                print_to_log(text='Too many login failures!', color=failed_color, i=i, total=total, account=account)

            except exceptions.EmailCodeRequired:
                account.status = Statuses.EmailGuard
                print_to_log(
                    text='The account is enabled to receive Steam Guard codes to the email!', color=failed_color, i=i,
                    total=total, account=account
                )

            except BaseException as e:
                logging.exception(f'check | {account.login}')
                print_to_log(text=f'ERROR: {e}', color=failed_color, i=i, total=total, account=account)

            db.commit()

    except BaseException as e:
        logging.exception('check')
        print_to_log(text=f'Something went wrong: {e}', color=failed_color)


color = config.GREEN
failed_color = config.RED
