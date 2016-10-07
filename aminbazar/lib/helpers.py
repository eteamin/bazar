# -*- coding: utf-8 -*-

"""WebHelpers used in twa."""

# from webhelpers import date, feedgenerator, html, number, misc, text
from tg import config, session
from sqlalchemy.orm import joinedload
from markupsafe import Markup
from datetime import datetime
from aminbazar import model
from khayyam import JalaliDate, JalaliDatetime, teh_tz


def current_year():
    now = datetime.now()
    return now.strftime('%Y')


def persian_date():
    return JalaliDate.today().strftime('%x')


def icon(icon_name):
    return Markup('<i class="glyphicon glyphicon-%s"></i>' % icon_name)


def is_debug():
    return config.get('debug')


def parent_menus():
    return model.DBSession.query(model.ParentMenu).order_by(model.ParentMenu.order)


def footer():
    return model.DBSession.query(model.Footer).first().content


def socials():
    return model.DBSession.query(model.Social).all()


def format_persian_date(d):
    return JalaliDate(d).strftime('%A %D %B %N')


def format_persian_datetime(d):
    return JalaliDatetime(d).strftime('%A %D %B %N %h:%r')


def get_model_class_by_name(class_name):
    return getattr(model, class_name)


def add_global_template_variables():
    return dict(
        related_links=model.DBSession.query(model.RelatedLink),
        dst=int(teh_tz.dst(JalaliDatetime.now()).total_seconds() / 3600),
        sponsors=model.DBSession.query(model.Sponsor).all(),
        tg_config=config,
        session=session,
        ads=model.DBSession.query(model.Ad).all(),
        categories=model.DBSession.query(model.Category).options(joinedload('sub_category')).order_by
        (model.Category.id).all(),
        )
