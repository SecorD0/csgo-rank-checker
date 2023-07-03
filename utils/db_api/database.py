from typing import List, Optional

from pretty_utils.databases import sqlalchemy_, sqlite

from data.config import ACCOUNTS_DB
from data.models import Statuses
from utils.db_api.tables import Account, Base


# --- Functions
def get_account(login: str, sqlite_query: bool = False) -> Optional[Account]:
    if sqlite_query:
        return sqlite.DB(ACCOUNTS_DB).execute('SELECT * FROM accounts WHERE login = ?', (login,), True)

    return db.one(Account, Account.login == login)


def get_accounts(sqlite_query: bool = False) -> List[Account]:
    if sqlite_query:
        return sqlite.DB(ACCOUNTS_DB).execute('SELECT * FROM accounts')

    return db.all(Account)


def get_unchecked_accounts(sqlite_query: bool = False) -> List[Account]:
    if sqlite_query:
        return sqlite.DB(ACCOUNTS_DB).execute('SELECT * FROM accounts WHERE status = ?', (Statuses.New,))

    return db.all(Account, Account.status.is_(Statuses.New))


# --- Miscellaneous
db = sqlalchemy_.DB('sqlite:///files/accounts.db', pool_recycle=3600, connect_args={'check_same_thread': False})

db.create_tables(Base)
