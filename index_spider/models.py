#! -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer, Decimal, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


DeclarativeBase = declarative_base()


def db_connect():

    return create_engine(URL(**settings.DATABASE))


def create_index_table(engine):
    
    DeclarativeBase.metadata.create_all(engine)


class IndexData(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "day_best"

    id = Column(Integer, primary_key=True)
    date = Column('date', DateTime, nullable=True)
    1 = Column('1', String, nullable=True)
    2 = Column('2', String, nullable=True)
    3 = Column('3', String, nullable=True)
    4 = Column('4', String, nullable=True)
    5 = Column('5', String, nullable=True)
    6 = Column('6', String, nullable=True)
    7 = Column('7', String, nullable=True)
    8 = Column('8', String, nullable=True)
    9 = Column('9', String, nullable=True)
    10 = Column('10', String, nullable=True)
    01 = Column('01', Decimal(5,2), nullable=True)
    02 = Column('02', Decimal(5,2), nullable=True)
    03 = Column('03', Decimal(5,2), nullable=True)
    04 = Column('04', Decimal(5,2), nullable=True)
    05 = Column('05', Decimal(5,2), nullable=True)
    06 = Column('06', Decimal(5,2), nullable=True)
    07 = Column('07', Decimal(5,2), nullable=True)
    08 = Column('08', Decimal(5,2), nullable=True)
    09 = Column('09', Decimal(5,2), nullable=True)
    010 = Column('010', Decimal(5,2), nullable=True)
