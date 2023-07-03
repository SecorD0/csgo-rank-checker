import glob
import os
from typing import Dict

from pretty_utils.miscellaneous.files import read_json

from data import config


def get_mafile_dict() -> Dict[str, str]:
    mafile_dict = {}
    mafiles = glob.glob(pathname=os.path.join(config.MAFILES_DIR, '*.maFile'))
    for mafile in mafiles:
        content = read_json(path=mafile)
        login = content.get('account_name')
        mafile_dict[login] = mafile

    return mafile_dict
