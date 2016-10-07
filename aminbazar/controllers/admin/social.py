# -*- coding: utf-8 -*-

from webhelpers import html
from tw2.forms import TextField, FileField, FileValidator, NumberField, UrlField
from aminbazar.model import Stuff
from tg import expose
from datetime import datetime
from .smart import SmartEasyCrudRestController


class SocialAdminController(SmartEasyCrudRestController):

    model = Stuff
    title = u'مداریت شبکه های اجتمائی'
    remember_values = ['image']

    __form_options__ = {
        '__hide_fields__': [],
        '__omit_fields__': ['entry_time', 'author', 'modified', 'modified_fa', 'entry_time_fa'],
        '__require_fields__': ['id', 'title', 'url', 'image'],
        '__field_order__': ['id', 'title', 'url', 'image'],
        '__field_widget_types__': {
            'id': NumberField,
            'title': TextField,
            'url': UrlField,
            'image': FileField,
            'order': NumberField
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
        return super(SocialAdminController, self).put(*args, **kw)
