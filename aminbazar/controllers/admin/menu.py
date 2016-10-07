# -*- coding: utf-8 -*-

from tw2.forms import TextField, TextArea, NumberField, SingleSelectField
from aminbazar.model import ParentMenu, SubMenu, DBSession, Menu
from .smart import SmartEasyCrudRestController
from tg import expose
from datetime import datetime
#from sprox.widgets import PropertySingleSelectField


class ParentField(SingleSelectField):
    options = DBSession.query(Menu).order_by(Menu.title)

    def _iterate_options(self, optlist):
        for item in optlist:
            if isinstance(item, (tuple, list)):
                yield item
            else:
                yield item.id, item.title


class MenuAdminController(SmartEasyCrudRestController):
    __form_options__ = {
        '__hide_fields__': [],
        '__omit_fields__': ['id', 'entry_time', 'author', 'row_type', 'modified', 'parent_id', 'modified_fa', 'entry_time_fa', '_header'],
        '__require_fields__': ['title',
                               'description',
                               'keywords',
                               'order',
                               'parent'],
        '__field_order__': ['title', 'description', 'keywords', 'order', 'address', 'content'],
        '__field_widget_types__': {'title': TextField,
                                   'address': TextField,
                                   'keywords': TextField,
                                   'order': NumberField,
                                   'description': TextArea,
                                   'parent': ParentField
                               },

    }

    __table_options__ = {
        '__omit_fields__': ['id', 'content', 'modified', 'entry_time', 'row_type', 'author_id', '_header'],
        '__headers__': {
            'entry_time_fa': 'entry_time',
            'modified_fa': 'modified'
        }
    }

    @expose(inherit=True)
    def put(self, *args, **kw):
        kw['modified'] = datetime.now()
        return super(MenuAdminController, self).put(*args, **kw)


class ParentMenuAdminController(MenuAdminController):
    model = ParentMenu
    title = "Parent Menu Administration"


class SubMenuAdminController(MenuAdminController):
    model = SubMenu
    title = "Sub Menu Administration"
