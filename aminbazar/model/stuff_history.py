# -*- coding: utf-8 -*-
"""Sample model module."""

from sqlalchemy import Column
from sqlalchemy.types import Integer, Unicode
from aminbazar.model.mixines import AuthoredMixin, OrderableMixin
from aminbazar.model import DeclarativeBase


class BossHistory(OrderableMixin, AuthoredMixin, DeclarativeBase):
    __tablename__ = 'boss_history'

    id = Column(Integer, primary_key=True)
    description = Column(Unicode(500), nullable=False)


class SecretaryHistory(OrderableMixin, AuthoredMixin, DeclarativeBase):
    __tablename__ = 'secretary_history'

    id = Column(Integer, primary_key=True)
    description = Column(Unicode(500), nullable=False)