from wheezy.routing import url
from wheezy.web.handlers import file_handler
from views import ListHandler, ViewHandler

all_urls = [
    url('', ListHandler, name='list'),
    url('album/{title}', ViewHandler, name='view_album'),
    url('static/{path:any}',
        file_handler(root='static/'),
        name='static')
]