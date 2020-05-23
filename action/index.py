from action.base import BaseHandler
from tornado.options import options
from serialize import blog
from serialize.jsonencoder import DatetimeEncoder
import json
class Index(BaseHandler):
    def get(self):
        list = self.db.only_sql('select url,title,content from article ORDER BY aid DESC LIMIT 0,10')#list
        if options.summary == "y":
            try:
                summary_list = blog.summary(list)
                self.render("index.html",list = summary_list)
            except:
                self.write("error, please check if the syntax is correct")
        else:
            self.render("index.html",list = list)