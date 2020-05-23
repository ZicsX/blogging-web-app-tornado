from action.base import BaseHandler
import dao


class About(BaseHandler):
    def get(self):
        self.render("page/about.html")

class Type(BaseHandler):
    def get(self):
        type1dc = dao.selectTypeArticle("type1")
        type2dc = dao.selectTypeArticle("type2")
        otherdc = dao.selectTypeArticle("post")
        self.render("page/type.html",type1 = type1dc,type2 = type2dc,other = otherdc)