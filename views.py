from wheezy.web.handlers import BaseHandler
from repository import Repository

from config import album_path


class ListHandler(BaseHandler):

	def get(self):
		repo = Repository(album_path)
		albums = repo.list_album() 
		return self.render_response('list.html',
				albums=albums)


class ViewHandler(BaseHandler):

	def get(self):
		repo = Repository(album_path)
		photos = repo.list_photos(self.route_args.get('title')) 
		return self.render_response('view.html',
				photos=photos)