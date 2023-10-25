import logging
import re
import time
from typing import Union

from bs4 import BeautifulSoup as BS
from pretty_utils.miscellaneous.time_and_date import unix_to_strtime
from pretty_utils.type_functions.strings import text_between
from steampy import exceptions
from steampy.client import SteamClient
from steampy.models import SteamUrl

from data import config
from data.models import Statuses, Settings
from functions.get_mafile_dict import get_mafile_dict
from utils.db_api.database import db, get_unchecked_accounts
from utils.miscellaneous.get_random_proxy import get_random_proxy
from utils.miscellaneous.print_to_log import print_to_log


def get_rank(steam_client: SteamClient, steam_id: Union[str, int]) -> int:
    html = steam_client._session.get(url=f'{SteamUrl.COMMUNITY_URL}/profiles/{steam_id}/gcpd/730')
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
                proxy = get_random_proxy()
                if 'http' not in proxy:
                    proxy = f'http://{proxy}'

                steam_client = SteamClient(api_key='', proxies={'http': proxy, 'https': proxy})
                steam_client.login(
                    username=account.login, password=account.password, steam_guard=mafiles[account.login]
                )
                account.status = Statuses.Checked
                steam_id = steam_client.get_steam_id()
                account.rank = get_rank(steam_client=steam_client, steam_id=steam_id)
                text = f'Rank: {account.rank}'
                if settings.parse.last_online:
                    try:
                        profile_page = steam_client._session.get(f'{SteamUrl.COMMUNITY_URL}/profiles/{steam_id}')
                        last_online = text_between(
                            text=profile_page.text, begin='<div class="profile_in_game_name">', end='</div>'
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

            except exceptions.InvalidCredentials:
                account.status = Statuses.WrongCredentials
                print_to_log(text='Wrong credentials!', color=failed_color, i=i, total=total, account=account)

            except exceptions.CaptchaRequired:
                print_to_log(text='Captcha required!', color=failed_color, i=i, total=total, account=account)

            except exceptions.ConfirmationExpected:
                account.status = Statuses.CodeRequired
                print_to_log(text='Confirmation code required!', color=failed_color, i=i, total=total, account=account)

            except exceptions.TooManyRequests:
                print_to_log(text='Too many login failures!', color=failed_color, i=i, total=total, account=account)

            except exceptions.ProxyConnectionError:
                print_to_log(text="The proxy doesn't work!", color=failed_color, i=i, total=total, account=account)

            except BaseException as e:
                logging.exception(f'check | {account.login}')
                print_to_log(text=f'ERROR: {e}', color=failed_color, i=i, total=total, account=account)

            db.commit()

    except BaseException as e:
        logging.exception('check')
        print_to_log(text=f'Something went wrong: {e}', color=failed_color)


color = config.GREEN
failed_color = config.RED
