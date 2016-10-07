# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import Integer, Unicode, Numeric
from aminbazar.model import DeclarativeBase
from aminbazar.model.mixines import OrderableMixin, AuthoredMixin
from tgtoolbox.model.attachment import AttachmentCleanerMixin, Attachment, AttachedImage


class Category(OrderableMixin, AuthoredMixin, AttachmentCleanerMixin, DeclarativeBase):
    __tablename__ = 'category'

    #{ Columns

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    image = Column(Attachment(AttachedImage), nullable=False)

    #}

Category.register_events()


class SubCategory(OrderableMixin, AuthoredMixin, AttachmentCleanerMixin, DeclarativeBase):
    __tablename__ = 'sub_category'

    #{ Columns

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    image = Column(Attachment(AttachedImage), nullable=False)
    category_id = Column(Integer, ForeignKey(
        'category.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    category = relationship('Category', backref=backref('sub_category'))
    #}

SubCategory.register_events()


class Product(OrderableMixin, AuthoredMixin, AttachmentCleanerMixin, DeclarativeBase):
    __tablename__ = 'product'

    #{ Columns

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=True)
    sub_category_id = Column(Integer, ForeignKey(
        'sub_category.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    sub_category = relationship('SubCategory', backref=backref('product'))

    year_of_production = Column(Unicode(255), nullable=True)
    country_of_production = Column(Unicode(255), nullable=True)
    quantity = Column(Unicode(255), nullable=False)
    price = Column(Unicode(255), nullable=False)
    image = Column(Attachment(AttachedImage), nullable=True)

    account_id = Column(Integer, ForeignKey(
        'account.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    account = relationship('Account', backref=backref('product'))

    #}

Product.register_events()
