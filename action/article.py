import tornado.web
from action.base import BaseHandler
import dao

class Article(BaseHandler):
    def get(self,url):
        data = dao.getArticle(url)
        print(data)
        self.render(
            "article.html",
            article = data,
            title = data['title']
        )
