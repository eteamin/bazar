
from tgext.crud.resources import crud_script, CSSSource
from tgext.admin.layouts import BootstrapAdminLayout
from tgext.admin.widgets import BootstrapAdminTableBase, \
    BootstrapAdminAddRecordForm, BootstrapAdminEditableForm, \
    BootstrapAdminTableFiller


class CustomAdminLayout(BootstrapAdminLayout):
    template_index = "aminbazar.templates.admin.index"
    crud_templates = {'get_all':    ['mako:aminbazar.templates.admin.bootstrap_crud.get_all'],
                      'edit':       ['mako:aminbazar.templates.admin.bootstrap_crud.edit'],
                      'new':        ['mako:aminbazar.templates.admin.bootstrap_crud.new']
    }
    crud_resources = [crud_script,
                      CSSSource(location='headbottom',
                                src='''
.crud-sidebar .active {
    font-weight: bold;
    border-left: 3px solid #eee;
}

@media (max-width: 991px) {
    .pull-sm-right {
        float: right;
    }
}

@media (min-width: 992px) {
    .pull-md-right {
        float: right;
    }
}
''')]

    TableBase = BootstrapAdminTableBase
    AddRecordForm = BootstrapAdminAddRecordForm
    EditableForm = BootstrapAdminEditableForm
    TableFiller = BootstrapAdminTableFiller