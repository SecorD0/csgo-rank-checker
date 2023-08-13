from typing import Optional

from pretty_utils.type_functions.classes import AutoRepr
from sqlalchemy import (Column, Integer, Text)
from sqlalchemy.orm import declarative_base

from data.models import Statuses

# --- Accounts
Base = declarative_base()


class Account(Base, AutoRepr):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    login = Column(Text, unique=True)
    password = Column(Text)
    status = Column(Text)
    rank = Column(Integer)
    last_online = Column(Integer)

    def __init__(
            self, login: str, password: str, status: str = Statuses.New, rank: Optional[int] = None,
            last_online: Optional[int] = None
    ) -> None:
        self.login = login
        self.password = password
        self.status = status
        self.rank = rank
        self.last_online = last_online
