# -*- coding: utf-8 -*-
from sqlalchemy import Column
from sqlalchemy.types import Integer, Unicode
from aminbazar.model.mixines import OrderableMixin, AuthoredMixin, ModifiedMixin
from aminbazar.model import DeclarativeBase
from tgtoolbox.model.attachment import AttachmentCleanerMixin, Attachment, AttachedImage



class RelatedLink(OrderableMixin, AuthoredMixin, ModifiedMixin, DeclarativeBase):
    __tablename__ = 'related_link'

    # { Columns

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(50), nullable=False, index=True)
    url = Column(Unicode(2048), nullable=False)

    # }


class RelatedImageLink(OrderableMixin, AttachmentCleanerMixin, AuthoredMixin, ModifiedMixin, DeclarativeBase):
    __tablename__ = 'related_image_link'

    # { Columns

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(50), nullable=False, index=True)
    image = Column(Attachment(AttachedImage), nullable=True)
    url = Column(Unicode(2048), nullable=False)

    # }

RelatedImageLink.register_events()