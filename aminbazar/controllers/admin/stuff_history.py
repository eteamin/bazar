# -*- coding: utf-8 -*-

from tw2.forms import TextField, NumberField
from aminbazar.model import BossHistory, SecretaryHistory
from .smart import SmartEasyCrudRestController
from tg import expose
from datetime import datetime


class BossHistoryAdminController(SmartEasyCrudRestController):
    model = BossHistory
    title = u'مدیریت سوابق مدیریت'
    __form_options__ = {
        '__hide_fields__': [],
        '__omit_fields__': ['id', 'entry_time', 'author', 'modified', 'modified_fa', 'entry_time_fa'],
        '__require_fields__': ['description'],
        '__field_order__': ['description'],
        '__field_widget_types__': {
            'description': TextField,
            'order': NumberField
        },
    }

    __table_options__ = {
        '__omit_fields__': ['id', 'content', 'author_id', 'modified', 'entry_time'],
        '__headers__': dict(
            modified_fa=u'تاریخ آخرین تغییر',
            entry_time_fa=u'تاریخ ثبت',
            description=u'محتوا',
            author=u'کاربر',
        )
    }

    @expose(inherit=True)
    def put(self, *args, **kw):
        kw['modified'] = datetime.now()
        return super(BossHistoryAdminController, self).put(*args, **kw)


class SecretaryHistoryAdminController(SmartEasyCrudRestController):
    model = SecretaryHistory
    title = u'مدیریت سوابق مدیریت'
    __form_options__ = {
        '__hide_fields__': [],
        '__omit_fields__': ['id', 'entry_time', 'author', 'modified', 'modified_fa', 'entry_time_fa'],
        '__require_fields__': ['description'],
        '__field_order__': ['description'],
        '__field_widget_types__': {
            'description': TextField,
            'order': NumberField
        },
    }

    __table_options__ = {
        '__omit_fields__': ['id', 'content', 'author_id', 'modified', 'entry_time'],
        '__headers__': dict(
            modified_fa=u'تاریخ آخرین تغییر',
            entry_time_fa=u'تاریخ ثبت',
            description=u'محتوا',
            author=u'کاربر',
        )
    }

    @expose(inherit=True)
    def put(self, *args, **kw):
        kw['modified'] = datetime.now()
        return super(SecretaryHistoryAdminController, self).put(*args, **kw)