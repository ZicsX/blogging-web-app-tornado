import markdown2
import tornado
from action.UserHandler import UserHandler
import dao
class Publish(UserHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("page/new_article.html")
    @tornado.web.authenticated
    def post(self):
        title = self.get_argument('title')
        cat = self.get_argument('cat')
        content = self.get_argument('content')
        url = self.get_argument('url')
        content = markdown2.unicode(markdown2.markdown(content))
        dao.addArticle(title,content,url,cat)
        self.redirect('/article/'+url)