import tornado.web
from action.base import BaseHandler
import dao

class Archive(BaseHandler):
    def get(self):
        data = dao.getArchive()
        self.render("archive.html",entries=data)
