# -*- coding: utf-8 -*-
"""Setup the twa application"""

from os.path import abspath, join, dirname, exists
from os import makedirs

from aminbazar.websetup.bootstrap.auth import bootstrap as membership_bootstrap
from aminbazar.websetup.bootstrap.root import bootstrap as root_bootstrap

HERE = abspath(dirname(__file__))
UPLOADS_DIR = abspath(join(HERE, '../../public/uploads/attachments'))


def bootstrap(command, conf, vars):
    """Place any commands to setup twa here"""

    if not exists(UPLOADS_DIR):
        makedirs(UPLOADS_DIR)

    membership_bootstrap(command, conf, vars)
    root_bootstrap(command, conf, vars)
