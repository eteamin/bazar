# -*- coding: utf-8 -*-
__author__ = 'vahid'
import tg.i18n
from tg import response
from datetime import timedelta


def set_lang(lang):
    tg.i18n.set_lang(lang)
    response.set_cookie('lang',
                        lang,
                        max_age=timedelta(days=500))


def get_lang():
    languages = tg.i18n.get_lang(all=False)
    if languages:
        return languages[0][:2]
    else:
        return None