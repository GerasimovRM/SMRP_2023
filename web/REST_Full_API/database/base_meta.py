import sqlalchemy.ext.declarative as dec
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

Base = dec.declarative_base()
engine = create_engine(f"sqlite:///db2.db")
session_factory = sessionmaker(bind=engine)


def get_session() -> Session:
    return session_factory()
