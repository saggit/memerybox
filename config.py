from wheezy.html.utils import html_escape
from wheezy.template.engine import Engine
from wheezy.template.ext.core import CoreExtension
from wheezy.template.loader import FileLoader
from wheezy.web.templates import WheezyTemplate

options = {}

# Template Engine
searchpath = ['templates']
engine = Engine(
    loader=FileLoader(searchpath),
    extensions=[
        CoreExtension(),
    ])
engine.global_vars.update({
    'h': html_escape
})
options.update({
    'render_template': WheezyTemplate(engine)
})

album_path = "static/album"