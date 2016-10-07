# -*- coding: utf-8 -*-
"""Setup the twa application"""
import transaction
from aminbazar.model import DBSession, ParentMenu, Footer, Stuff


def bootstrap(command, conf, vars):
    """Place any commands to setup twa here"""

    from sqlalchemy.exc import IntegrityError
    website_title = u'امین بازار'
    try:

        # Menus
        home = ParentMenu(
            id=1,
            order=1,
            title=u'خانه',
            header=website_title,
            description=u'',
            address=u'/')

        DBSession.add(home)
        # Footer
        DBSession.add(Footer(content=u'تمامی حقوق این سایت برای %s محفوظ می‌باشد.' % website_title))

        # Banners

        DBSession.add(Stuff(id=1, title=u'Boss', job_title=u'Shit'))
        DBSession.add(Stuff(id=2, title=u'secretary', job_title=u'Shit'))
        DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print('Warning, there was a problem adding your data, it may have already been added:')
        import traceback

        print(traceback.format_exc())
        transaction.abort()
        print('Continuing with bootstrapping...')