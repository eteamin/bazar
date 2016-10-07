# -*- coding: utf-8 -*-
"""Sample model module."""


from sqlalchemy import Column
from sqlalchemy.types import Integer, Unicode
from aminbazar.model.mixines import OrderableMixin, AuthoredMixin
from aminbazar.model import DeclarativeBase
from tgtoolbox.model.attachment import AttachmentCleanerMixin, Attachment, AttachedImage


class Sponsor(OrderableMixin, AttachmentCleanerMixin, AuthoredMixin, DeclarativeBase):
    __tablename__ = 'sponsor'

    #{ Columns

    id = Column(Integer, primary_key=True)
    url = Column(Unicode(255), nullable=False)
    image = Column(Attachment(AttachedImage), nullable=False)

    #}

Sponsor.register_events()