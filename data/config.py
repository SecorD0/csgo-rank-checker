import os
import platform
import sys
from pathlib import Path

from colorama import Fore, Style

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()

else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

if platform.system() == 'Windows':
    GREEN = ''
    LIGHTGREEN_EX = ''
    RED = ''
    RESET_ALL = ''

else:
    GREEN = Fore.GREEN
    LIGHTGREEN_EX = Fore.LIGHTGREEN_EX
    RED = Fore.RED
    RESET_ALL = Style.RESET_ALL

FILES_DIR = os.path.join(ROOT_DIR, 'files')
MAFILES_DIR = os.path.join(FILES_DIR, 'maFiles')

ACCOUNTS_DB = os.path.join(FILES_DIR, 'accounts.db')

ERRORS_FILE = os.path.join(FILES_DIR, 'errors.log')

ACCOUNTS_FILE = os.path.join(FILES_DIR, 'accounts.xlsx')
PROXIES_FILE = os.path.join(FILES_DIR, 'proxies.txt')
SETTINGS_FILE = os.path.join(FILES_DIR, 'settings.json')

VERSION = '2.1.0'
