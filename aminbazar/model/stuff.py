# -*- coding: utf-8 -*-
"""Sample model module."""

from sqlalchemy import Column
from sqlalchemy.types import Integer, Unicode
from aminbazar.model.mixines import AuthoredMixin, OrderableMixin
from aminbazar.model import DeclarativeBase
from tgtoolbox.model.attachment import AttachmentCleanerMixin, Attachment, AttachedImage


class Stuff(OrderableMixin, AttachmentCleanerMixin, AuthoredMixin, DeclarativeBase):
    __tablename__ = 'stuff'
    __edit_only__ = True

    id = Column(Integer, primary_key=True, autoincrement=False)
    title = Column(Unicode(100), nullable=False)
    job_title = Column(Unicode(100), nullable=False)
    image = Column(Attachment(AttachedImage), nullable=True)


Stuff.register_events()
