# -*- coding: utf-8 -*-
import os
from datetime import datetime
from sqlalchemy.types import DateTime
from hashlib import sha256
from sqlalchemy import Column
from sqlalchemy.orm import synonym
from sqlalchemy.types import Integer, Unicode
from tgtoolbox.model.attachment import AttachmentCleanerMixin, Attachment, AttachedImage

from aminbazar.model.mixines import OrderableMixin, AuthoredMixin
from aminbazar.model import DeclarativeBase
__author__ = 'juggerpy'


class Account(OrderableMixin, AuthoredMixin, AttachmentCleanerMixin, DeclarativeBase):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    user_name = Column(Unicode(255), unique=True, nullable=False)
    email_address = Column(Unicode(255), unique=True, nullable=True)
    bio = Column(Unicode(1000), nullable=False)
    _password = Column('password', Unicode(128))
    creation_time = Column(DateTime, default=datetime.now)

    @classmethod
    def _hash_password(cls, password):
        salt = sha256()
        salt.update(os.urandom(60))
        salt = salt.hexdigest()

        hash = sha256()
        hash.update((password + salt).encode('utf-8'))
        hash = hash.hexdigest()

        password = salt + hash
        password = password.decode('utf-8')

        return password

    def _set_password(self, password):
        self._password = self._hash_password(password)

    def _get_password(self):
        return self._password

    password = synonym('_password', descriptor=property(_get_password,
                                                        _set_password))

    def validate_password(self, password):
        hash = sha256()
        hash.update((password + self.password[:64]).encode('utf-8'))
        return self.password[64:] == hash.hexdigest()


__all__ = ['Account']
