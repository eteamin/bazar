# -*- coding: utf-8 -*-
"""Sample model module."""


from sqlalchemy import Column
from sqlalchemy.types import Integer, Unicode
from aminbazar.model.mixines import OrderableMixin, AuthoredMixin
from aminbazar.model import DeclarativeBase
from tgtoolbox.model.attachment import AttachmentCleanerMixin, Attachment, AttachedImage


class Banner(OrderableMixin, AttachmentCleanerMixin, AuthoredMixin, DeclarativeBase):
    __tablename__ = 'banner'

    #{ Columns

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=True)
    image = Column(Attachment(AttachedImage), nullable=True)

    #}

Banner.register_events()