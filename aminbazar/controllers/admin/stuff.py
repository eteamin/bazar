# -*- coding: utf-8 -*-

from tw2.forms import TextField, FileField, FileValidator, NumberField
from webhelpers import html
from aminbazar.model import Stuff
from tg import expose
from datetime import datetime
from .smart import SmartEasyCrudRestController


class StuffAdminController(SmartEasyCrudRestController):

    model = Stuff
    title = u'مداریت سمتها'
    remember_values = ['image']

    __form_options__ = {
        '__hide_fields__': [],
        '__omit_fields__': ['entry_time', 'author', 'modified', 'modified_fa', 'entry_time_fa'],
        '__require_fields__': ['id', 'title', 'job_title', 'image'],
        '__field_order__': ['id', 'title', 'job_title', 'image'],
        '__field_widget_types__': {
            'id': NumberField,
            'title': TextField,
            'job_title': TextField,
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
        return super(StuffAdminController, self).put(*args, **kw)
