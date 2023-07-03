from pretty_utils.miscellaneous.files import touch

from data import config
from utils.miscellaneous.create_spreadsheet import create_spreadsheet


def create_files():
    touch(path=config.FILES_DIR)
    touch(path=config.MAFILES_DIR)
    create_spreadsheet(path=config.ACCOUNTS_FILE, headers=('login', 'password'), sheet_name='Accounts')
    touch(path=config.PROXIES_FILE, file=True)


create_files()
