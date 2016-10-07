# -*- coding: utf-8 -*-

from tw2.forms import FileField, FileValidator, NumberField, TextField
from webhelpers import html
from .smart import SmartEasyCrudRestController
from aminbazar.model import Banner
from datetime import datetime
from tg import expose


class BannerAdminController(SmartEasyCrudRestController):
    model = Banner
    remember_values = ['image']
    title = "Banner Administration"

    __form_options__ = {
        '__hide_fields__': [],
        '__omit_fields__': ['id', 'entry_time', 'author', 'modified', 'modified_fa', 'entry_time_fa'],
        '__field_order__': ['title', 'image'],
        '__field_widget_types__': {'image': FileField,
                                   'title': TextField,
                                   'order': NumberField},
        '__field_validator_types__': {'image': FileValidator},
    }

    __table_options__ = {
        '__omit_fields__': ['id', 'entry_time', 'author_id', 'modified'],
        '__xml_fields__': ['image'],
        'image': lambda filler, row: html.literal(
            row.image and '<img class="datatable-image" src="%s"/>' % row.image.thumb_url or '<span>no image</span>'),
        '__headers__': dict(
            modified_fa=u'تاریخ آخرین تغییر',
            entry_time_fa=u'تاریخ ثبت',
            title=u'عنوان',
            order=u'ترتیب',
            image=u'تصویر',
            author=u'کاربر',

        )
    }

    @expose(inherit=True)
    def put(self, *args, **kw):
        kw['modified'] = datetime.now()
        return super(BannerAdminController, self).put(*args, **kw)
