
from tw2.tinymce import TinyMCEWidget
import tw2.core as twc

#elfinder_dir = twc.DirLink(modname=__name__, filename="static/elFinder")
elfinder_js = twc.JSLink(modname = 'twa' , filename = 'public/contrib/elfinder/tinymce.integrate.js')

class TinyMCEelFinderWidget(TinyMCEWidget):
    mce_options= dict(file_browser_callback = 'elFinderBrowser', directionality = 'rtl')
    resources = TinyMCEWidget.resources + [elfinder_js]