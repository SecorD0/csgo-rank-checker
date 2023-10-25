from dataclasses import dataclass

from pretty_utils.miscellaneous.files import read_json
from pretty_utils.type_functions.classes import AutoRepr, Singleton

from data import config


# ----- Settings
@dataclass
class Parse:
    last_online: bool


class Settings(Singleton, AutoRepr):
    def __init__(self) -> None:
        json = read_json(path=config.SETTINGS_FILE)

        # --- Parse
        parse = json['parse']
        self.parse = Parse(
            last_online=parse['last_online']
        )


# ----- Script
class Statuses:
    New = 'new'
    WrongCredentials = 'wrong credentials'
    CodeRequired = 'code required'
    Checked = 'checked'
