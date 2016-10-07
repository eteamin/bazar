# -*- coding: utf-8 -*-
from sqlalchemy import Column
from sqlalchemy.orm import deferred
from sqlalchemy.types import Integer, UnicodeText
from aminbazar.model.mixines import AuthoredMixin, ModifiedMixin
from aminbazar.model import DeclarativeBase


class Footer(AuthoredMixin, ModifiedMixin, DeclarativeBase):
    __tablename__ = 'footer'
    
    #{ Columns
    
    id = Column(Integer, primary_key=True)
    content = deferred(Column(UnicodeText, nullable=False))

    #}

