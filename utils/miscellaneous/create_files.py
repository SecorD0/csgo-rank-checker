from typing import Optional

from pretty_utils.miscellaneous.files import touch, write_json, read_json
from pretty_utils.type_functions.dicts import update_dict

from data import config
from utils.miscellaneous.create_spreadsheet import create_spreadsheet


def create_files():
    touch(path=config.FILES_DIR)
    touch(path=config.MAFILES_DIR)
    create_spreadsheet(path=config.ACCOUNTS_FILE, headers=('login', 'password'), sheet_name='Accounts')
    touch(path=config.PROXIES_FILE, file=True)

    try:
        current_settings: Optional[dict] = read_json(path=config.SETTINGS_FILE)

    except:
        current_settings = {}

    settings = {
        'parse': {
            'rank': True,
            'last_online': False
        }
    }
    write_json(path=config.SETTINGS_FILE, obj=update_dict(modifiable=current_settings, template=settings), indent=2)


create_files()
