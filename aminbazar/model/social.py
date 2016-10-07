# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy.types import Integer, Unicode
from aminbazar.model.mixines import AuthoredMixin, OrderableMixin
from aminbazar.model import DeclarativeBase
from tgtoolbox.model.attachment import AttachmentCleanerMixin, Attachment, AttachedImage


class Social(OrderableMixin, AttachmentCleanerMixin, AuthoredMixin, DeclarativeBase):
    __tablename__ = 'social'

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(100), nullable=False)
    url = Column(Unicode(100), nullable=False)
    image = Column(Attachment(AttachedImage), nullable=True)


Social.register_events()
