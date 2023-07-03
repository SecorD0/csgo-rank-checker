from typing import Optional, Any

from pretty_utils.miscellaneous.time_and_date import unix_to_strtime

from data import config
from utils.db_api.tables import Account


def print_to_log(text: Any, color: Optional[str] = '', i: Optional[int] = None, total: Optional[int] = None,
                 account: Optional[Account] = None) -> None:
    printable_text = f'{unix_to_strtime()}'
    if account:
        printable_text += f' | {account.login}'
        if i is not None and total is not None:
            printable_text += f' ({i + 1}/{total})'

    printable_text += f' | {text}'
    print(color + printable_text + config.RESET_ALL)
