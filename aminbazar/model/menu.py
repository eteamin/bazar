# -*- coding: utf-8 -*-
from sqlalchemy import ForeignKey, Column
from sqlalchemy.orm import relationship, backref, deferred, synonym
from sqlalchemy.sql.schema import Sequence
from sqlalchemy.types import Integer, Unicode, UnicodeText, String
from aminbazar.model.mixines import OrderableMixin, AuthoredMixin, ModifiedMixin
from aminbazar.model import DeclarativeBase
import urllib


class Menu(OrderableMixin, AuthoredMixin, ModifiedMixin, DeclarativeBase):
    __tablename__ = 'menu'

    # { Columns

    id = Column(Integer, Sequence('menu_seq', start=100, increment=1), primary_key=True)
    title = Column(Unicode(30), nullable=False, index=True)
    # _caption = Column(Unicode(30), nullable=False)
    _header = Column(Unicode(200), nullable=True)
    description = Column(Unicode(100), nullable=True)
    address = Column(Unicode(500), nullable=True)
    content = deferred(Column(UnicodeText, nullable=True))
    row_type = Column(String(20))

    # }

    submenus = relationship("SubMenu",
                            backref=backref("parent", remote_side=[id]),
                            order_by=OrderableMixin.order)

    __mapper_args__ = {
        'polymorphic_on': row_type,
        'polymorphic_identity': 'menu'
    }

    def _set_header(self, title):
        self._header = title

    def _get_header(self):
        return self._header if self._header else self.title

    header = synonym('_header',
                     descriptor=property(_get_header, _set_header))

    # def _set_caption(self, title):
    #     self._caption = title
    #
    # def _get_caption(self):
    #     return self._caption if self._caption else self.title
    #
    # caption = synonym('_caption',
    #                  descriptor=property(_get_caption, _set_caption))

    @property
    def url_safe_title(self):
        return urllib.quote(self.title.encode('utf8'))

    @property
    def url(self):
        if self.address:
            return self.address
        elif self.content:
            return '/pages/%(id)s/%(title)s' % dict(id=self.id, title=self.url_safe_title)
        else:
            return None

    @property
    def last_modification_time(self):
        return self.modified if self.modified else self.entry_time

    @property
    def priority(self):
        order = self.order if self.order > 0 else 100
        return '%.1F' % (1.0 / order * 10)


class ParentMenu(Menu):
    __mapper_args__ = {
        'polymorphic_identity': 'parent_menu'
    }


class SubMenu(Menu):
    parent_id = Column(Integer, ForeignKey('menu.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'sub_menu'
    }
