import logging

from utils.miscellaneous.create_files import create_files
from data import config
from functions.General import General
from functions.check import check
from utils.db_api.database import db, get_accounts
from utils.miscellaneous.get_random_proxy import get_random_proxy

if __name__ == '__main__':
    try:
        create_files()
        General.import_accounts()
        if get_accounts():
            if get_random_proxy():
                try:
                    file = open(file=config.ACCOUNTS_FILE, mode='r+')
                    check()
                    General.export_accounts()
                    db.execute('DROP TABLE accounts')

                except IOError:
                    print(f"\n{config.RED}You didn't close the {config.ACCOUNTS_FILE} file!{config.RESET_ALL}")

            else:
                print(f"\n{config.RED}You didn't add HTTP IPv4 proxies to the proxies.txt file!{config.RESET_ALL}")

        else:
            print(f'\n{config.RED}There are no accounts!{config.RESET_ALL}')

    except BaseException as e:
        logging.exception('main')
        print(f'\n{config.RED}Something went wrong: {e}{config.RESET_ALL}\n')

    input(f'\nPress {config.LIGHTGREEN_EX}Enter{config.RESET_ALL} to exit.\n')
