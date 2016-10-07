# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Enum, DateTime, Integer, Unicode
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr
from aminbazar.model import DBSession
from datetime import datetime
from khayyam import JalaliDatetime
from tg import request

__all__ = [
    'TimestampMixin',
    'ModifiedMixin',
    'AuthoredMixin',
    'OrderableMixin',
    'ConfirmableMixin'
]

PERSIAN_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def persian_now():
    return JalaliDatetime.now().strftime(PERSIAN_DATE_FORMAT)


class TimestampMixin(object):
    entry_time = Column(DateTime, default=datetime.now, nullable=False)
    entry_time_fa = Column(Unicode(20), default=persian_now, nullable=False)

    @classmethod
    def get_recent(cls):
        return DBSession.query(cls).order_by(cls.entry_time.desc())


class ModifiedMixin(TimestampMixin):
    modified = Column(DateTime, nullable=True)
    modified_fa = Column(Unicode(20), default=persian_now, nullable=True)

    @property
    def last_modification_time(self):
        return self.modified if self.modified else self.entry_time


class AuthoredMixin(ModifiedMixin):

    @staticmethod
    def get_current_user_id():
        try:
            return request.identity['user'].id
        except:
            return 1
        # if request and hasattr(request, 'identity') and request.identity.get('repoze.who.userid'):
        #     userid = request.identity['user'].id
        #     return userid

    @declared_attr
    def author_id(cls):
        return Column("author_id", Integer, ForeignKey('user.id'), default=cls.get_current_user_id)

    @declared_attr
    def author(cls):
        return relationship("User")


class OrderableMixin(object):
    order = Column("order", Integer, default=0, nullable=False)
    __mapper_args__ = dict(order_by=order)


class ConfirmableMixin(object):
    status = Column(Enum('pending', 'confirmed', name="foreign_word_status"), default='pending', nullable=True)
    confirm_time = Column(DateTime, nullable=True)

    def confirm(self):
        self.status = 'confirmed'
        self.confirm_time = datetime.now()
