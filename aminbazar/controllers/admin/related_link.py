# -*- coding: utf-8 -*-

from tw2.forms import TextField, UrlField, FileField, FileValidator, NumberField
from webhelpers import html
from aminbazar.model import RelatedLink, RelatedImageLink
from tg import expose
from datetime import datetime
from .smart import SmartEasyCrudRestController


class RelatedLinkAdminController(SmartEasyCrudRestController):
    model = RelatedLink
    title = u'مدیریت پیوندها'

    __form_options__ = {
        '__hide_fields__': [],
        '__omit_fields__': ['id', 'entry_time', 'author', 'modified', 'modified_fa', 'entry_time_fa'],
        '__require_fields__': ['title', 'url'],
        '__field_order__': ['title', 'url'],
        '__field_widget_types__': {
            'title': TextField,
            'url': UrlField,
            'order': NumberField
        },
    }

    __table_options__ = {
        '__omit_fields__': ['id', 'content', 'author_id', 'modified', 'entry_time'],

    }

    @expose(inherit=True)
    def put(self, *args, **kw):
        kw['modified'] = datetime.now()
        return super(RelatedLinkAdminController, self).put(*args, **kw)


class RelatedImageLinkAdminController(SmartEasyCrudRestController):
    model = RelatedImageLink
    title = u'مدیریت پیوندهای تصویری'
    remember_values = ['image']

    __form_options__ = {
        '__hide_fields__': [],
        '__omit_fields__': ['id', 'entry_time', 'author', 'modified', 'modified_fa', 'entry_time_fa'],
        '__require_fields__': ['title', 'url'],
        '__field_order__': ['title', 'url', 'image'],
        '__field_widget_types__': {
            'title': TextField,
            'url': UrlField,
            'image': FileField,
            'order': NumberField
        },
        '__field_validator_types__': {'image': FileValidator},
    }

    __table_options__ = {
        '__omit_fields__': ['id', 'content', 'author_id', 'modified', 'entry_time'],
        '__xml_fields__': ['image'],
        'image': lambda filler, row: html.literal(
            row.image and '<img class="datatable-image" src="%s"/>' % row.image.thumb_url or '<span>no image</span>'),
    }

    @expose(inherit=True)
    def put(self, *args, **kw):
        kw['modified'] = datetime.now()
        return super(RelatedImageLinkAdminController, self).put(*args, **kw)