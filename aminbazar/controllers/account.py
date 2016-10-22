# -*- coding: utf-8 -*-
"""Account Controller"""
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from tg import expose, lurl, session, flash, lurl, abort, config as tg_config
from tg.i18n import ugettext as _
from tg.exceptions import HTTPFound
import transaction
from aminbazar.model import DBSession, Account
from aminbazar.lib.base import BaseController
from . import FakePage


__all__ = ['AccountController']


class AccountController(BaseController):

    @expose('aminbazar.templates.sign_up')
    def sign_up(self):
        return dict(
            page=FakePage(u'ثبت نام')
        )

    @expose('aminbazar.templates.sign_in')
    def sign_in(self):
        return dict(page=FakePage(header=u'ورود به حساب کاربری'))

    @expose()
    def login(self, **kwargs):
        try:
            user_name = kwargs['user_name']
            password = kwargs['password']
            try:
                account = DBSession.query(Account).filter(Account.user_name == user_name).one()
            except NoResultFound:
                flash(u'نام کاربری و یا رمز عبور اشتباه است', 'warning')
                return HTTPFound(location=lurl('/accounts/sign_in'))
            if account.validate_password(password):
                session['account_id'] = account.id
                session['user_name'] = account.user_name
                session.save()
                return HTTPFound(location=lurl('/'))
            else:
                flash(u'نام کاربری و یا رمز عبور اشتباه است', 'warning')
                return HTTPFound(location=lurl('/accounts/sign_in'))
        except KeyError:
            abort(400)

    @expose()
    def log_out(self):
        session.delete()
        return HTTPFound(location=lurl('/'))

    @expose()
    def register(self, **kwargs):

        recaptcha_secret = tg_config.get('recaptcha.private_key')
        recaptcha_url = tg_config.get('recaptcha.url')
        try:
            user_name = kwargs['user_name']
            email_address = kwargs['email_address']
            # recaptcha_resp = kwargs['g-recaptcha-response']
            password = kwargs['password']
            bio = kwargs['bio']
        except KeyError:
            abort(400)

        # Validating recaptcha-resp
        # google_recaptcha_resp = requests.post(
        #     recaptcha_url,
        #     data={
        #         'secret': recaptcha_secret,
        #         'response': recaptcha_resp,
        #     }
        # ).json()

        # if google_recaptcha_resp['success']:
        account = Account(
            user_name=user_name,
            email_address=email_address,
            password=password,
            bio=bio
        )
        try:
            DBSession.add(account)
            transaction.commit()
            flash(u'ثبت نام با موفقیت انجام شد')
            return HTTPFound(location=lurl('/accounts/sign_in'))
        except IntegrityError:
            transaction.abort()
            flash(u'این نام کاربری قبلا ثبت شده است', 'warning')
            return HTTPFound(location=lurl('/accounts/sign_up'))
