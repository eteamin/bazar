# -*- coding: utf-8 -*-
"""Main Controller"""
from tg import expose, flash, lurl, request, redirect, tmpl_context, abort, config as tg_config
from tg.render import render
from tg.i18n import ugettext as _
from tg.exceptions import HTTPFound
from aminbazar import model
from aminbazar.model import DBSession
from aminbazar.lib.base import BaseController
from sqlalchemy import or_
from .admin import LocalAdminController
from .error import ErrorController
from .products import ProductsController
from .account import AccountController


__all__ = ['RootController']


class RootController(BaseController):

    area52 = LocalAdminController(DBSession)
    error = ErrorController()
    account = AccountController()
    products = ProductsController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "aminbazar"
        if request.client_info.browser.family.lower() == 'ie' \
                and request.client_info.browser.version[0] <= 8:
            if not request.path.startswith('/incompatible'):
                redirect('/incompatible')

    @expose('aminbazar.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(
            products=model.DBSession.query(model.Product).all(),
            page=model.DBSession.query(model.ParentMenu).filter(model.Menu.id == 1).one(),
            banners=model.DBSession.query(model.Banner),
            related_image_links=model.DBSession.query(model.RelatedImageLink).all(),
        )

    @expose('aminbazar.templates.incompatible')
    def incompatible(self):
        """Handle the front-page."""
        abort(404)

    @expose('aminbazar.templates.login')
    def login(self, came_from=lurl('/'), failure=None, login=''):
        """Start the user login."""
        if failure is not None:
            if failure == 'user-not-found':
                flash(_('User not found'), 'error')
            elif failure == 'invalid-password':
                flash(_('Invalid Password'), 'error')

        login_counter = request.environ.get('repoze.who.logins', 0)
        if failure is None and login_counter > 0:
            flash(_('Wrong credentials'), 'warning')
        return dict(page='login', login_counter=str(login_counter),
                    came_from=came_from, login=login)

    @expose()
    def post_login(self, came_from=lurl('/')):

        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login',
                params=dict(came_from=came_from, __logins=login_counter))
        userid = request.identity['repoze.who.userid']
        flash(_('Welcome back, %s!') % userid)

        # Do not use tg.redirect with tg.url as it will add the mountpoint
        # of the application twice.
        return HTTPFound(location=came_from)

    @expose()
    def post_logout(self, came_from=lurl('/')):

        flash(_('We hope to see you soon!'))
        return HTTPFound(location=came_from)
