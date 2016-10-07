# -*- coding: utf-8 -*-
from tgext.crud import EasyCrudRestController
from tgext.crud.utils import RequestLocalTableFiller
from aminbazar.model import DBSession


class NormalTableFiller(RequestLocalTableFiller):
    def get_value(self, values=None, **kw):
        if 'order_by' not in kw:
            kw['order_by'] = 'entry_time'
            kw['desc'] = True
        return super(NormalTableFiller, self).get_value(values=values, **kw)


class EditOnlyTableFiller(NormalTableFiller):
    # __entity__ = Stuff

    def __actions__(self, obj):
        """Override this function to define how action links should be displayed for the given record."""
        primary_fields = self.__provider__.get_primary_fields(self.__entity__)
        pklist = '/'.join(map(lambda x: str(getattr(obj, x)), primary_fields))
        return '''
<a href="%(pklist)s/edit" class="btn btn-primary">
    <span class="glyphicon glyphicon-pencil"></span>
</a>
        ''' % dict(pklist=pklist)


class SmartEasyCrudRestController(EasyCrudRestController):

    def __init__(self, *args, **kw):
        if hasattr(self.model, '__edit_only__') and self.model.__edit_only__:
            self.table_filler = EditOnlyTableFiller(DBSession)
        else:
            self.table_filler = NormalTableFiller(DBSession)
        self.table_filler.__entity__ = self.model

        super(SmartEasyCrudRestController, self).__init__(*args, **kw)