# -*- coding: utf-8 -*-
# quickstarted Options:
#
# sqlalchemy: True
# auth:       sqlalchemy
# mako:       True
#
#

# install it by: pip install --process-dependency-links --trusted-host guthub.com --trusted-host dobisel.com -e .

#This is just a work-around for a Python2.7 issue causing
#interpreter crash at exit when trying to log an info message.
try:
    import logging
    import multiprocessing
except:
    pass

import sys

py_version = sys.version_info[:2]

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools

    use_setuptools()
    from setuptools import setup, find_packages

testpkgs = ['WebTest >= 1.2.3',
            'nose',
            'coverage',
            'gearbox'
            ]

install_requires = [
    "TurboGears2 >= 2.3.4",
    "Babel",
    "Genshi",
    "Mako",
    "zope.sqlalchemy >= 0.4",
    "sqlalchemy",
    "alembic",
    "repoze.who",
    "tw2.forms",
    "tgext.admin >= 0.6.1",
#    "tw2.tinymce",
    "tw2.recaptcha",
    "maryjane>=2.16",
    "psycopg2",
    "khayyam>=1.0.2",
    "webhelpers",
    "user-agents",
    # "tw2.bootstrap.forms>=2.2.4",
 #   "tgtoolbox>=0.16",
    "requests"
]


dependency_links = [
    "git+ssh://git@dobisel.com:9175/tg-toolbox.git@master#egg=tg-toolbox-0.16"
]

setup(
    name='aminbazar',
    version='0.1',
    description='',
    author='Amin Etesamian',
    author_email='aminetesamian1371@gmail.com',
    #url='',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=install_requires,
    dependency_links=dependency_links,
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=testpkgs,
    package_data={'aminbazar': ['i18n/*/LC_MESSAGES/*.mo',
                                    'templates/*/*',
                                    'public/*/*']},
    message_extractors={'aminbazar': [
        ('**.py', 'python', None),
        ('templates/**.mak', 'mako', None),
        ('public/**', 'ignore', None)]},

    entry_points={
        'paste.app_factory': [
            'main = aminbazar.config.middleware:make_app'
        ],
        'gearbox.plugins': [
            'turbogears-devtools = tg.devtools'
        ]
    },
    zip_safe=False
)
