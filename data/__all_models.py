import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'persons'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    last_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    result = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    from_id = sqlalchemy.Column(sqlalchemy.String,
                                index=True, unique=True, nullable=True)
    result_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                    default=datetime.datetime.now)
    opened = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    play_now = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)


class Info(SqlAlchemyBase):
    __tablename__ = 'citys'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    city = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    fact = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    photo_id = sqlalchemy.Column(sqlalchemy.String,
                                 index=True, unique=True, nullable=True)


class WorkWithPeople(SqlAlchemyBase):
    __tablename__ = 'work_with_people'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    city = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    local_id = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    from_id = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    right = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
