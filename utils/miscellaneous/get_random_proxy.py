import random
from typing import Optional

from pretty_utils.miscellaneous.files import read_lines

from data import config


def get_random_proxy() -> Optional[str]:
    proxies = read_lines(path=config.PROXIES_FILE, skip_empty_rows=True)
    if proxies:
        return random.choice(proxies)
