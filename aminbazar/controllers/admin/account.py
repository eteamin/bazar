# -*- coding: utf-8 -*-

from webhelpers import html
from tw2.forms import TextField, FileField, FileValidator, PasswordField, EmailField, NumberField
from aminbazar.model import Account
from tg import expose
from datetime import datetime
from .smart import SmartEasyCrudRestController


class AccountAdminController(SmartEasyCrudRestController):

    model = Account
    title = u'مدیریت کاربران'
    remember_values = ['image']

    __form_options__ = {
        '__hide_fields__': [],
        '__omit_fields__': [
            'entry_time',
            'author',
            'modified',
            'modified_fa',
            'entry_time_fa',
            'creation_time',
            'password'
        ],
        '__require_fields__': ['user_name', 'image'],
        '__field_order__': ['user_name', 'email_address', 'image'],
        '__field_widget_types__': {
            'user_name': TextField,
            'email_address': EmailField,
            'image': FileField,
            'password': PasswordField
        },
        '__field_validator_types__': {'image': FileValidator},
    }

    __table_options__ = {
        '__omit_fields__': ['author_id', 'modified', 'entry_time'],
        '__xml_fields__': ['image'],
        'image': lambda filler, row: html.literal(
            row.image and '<img class="datatable-image" src="%s"/>' % row.image.thumb_url or '<span>no image</span>'),
    }

    @expose(inherit=True)
    def put(self, *args, **kw):
        kw['modified'] = datetime.now()
        return super(AccountAdminController, self).put(*args, **kw)
