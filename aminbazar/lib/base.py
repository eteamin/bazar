# -*- coding: utf-8 -*-

"""The base Controller API."""

from tg import TGController, tmpl_context, config
from aminbazar.lib.i18n import get_lang, set_lang
from tg import request
import user_agents

__all__ = ['BaseController']


class BaseController(TGController):
    """
    Base class for the controllers in the application.

    Your web application should have one of these. The root of
    your application is used to compute URLs used by your app.

    """

    def __call__(self, environ, context):
        """Invoke the Controller"""
        # TGController.__call__ dispatches to the Controller method
        # the request is routed to.
        selected_lang = request.cookies.get('lang')
        if not selected_lang:
            selected_lang = config.get('lang')

        set_lang(selected_lang)

        request.identity = \
            tmpl_context.identity = request.environ.get('repoze.who.identity')

        request.language = \
            tmpl_context.lang = get_lang()

        request.client_info = user_agents.parse(request.user_agent)

        tmpl_context.project_name = "twa"

        return TGController.__call__(self, environ, context)