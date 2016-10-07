# -*- coding: utf-8 -*-
from tg.i18n import ugettext as _
from tw2.recaptcha import ReCaptchaWidget as BadRecaptchaWidget
from tw2.recaptcha.validator import ReCaptchaValidator as BadReCaptchaValidator
__author__ = 'vahid'


class ReCaptchaWidget(BadRecaptchaWidget):
    """
    Hack by Vahid Mardani, due the tw2.recaptcha validation bug
    """
    _sub_compound = True
    pass


class ReCaptchaValidator(BadReCaptchaValidator):
    """
    Hack by Vahid Mardani, due the tw2.recaptcha validation bug
    """
    not_empty = True
    messages = {
        'incorrect': _("Incorrect value."),
        'missing':  _("Missing value."),
    }