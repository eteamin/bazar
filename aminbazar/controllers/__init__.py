# -*- coding: utf-8 -*-
"""Controllers for the twa application."""


class FakePage(object):
    header = u''
    title = u''
    description = u''

    def __init__(self, header, description=None):
        self.title = self.header = header
        self.description = description
