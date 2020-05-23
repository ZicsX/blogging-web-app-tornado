from action.UserHandler import UserHandler
import bcrypt
import dao
import random
import time

class AuthCreateHandler(UserHandler):
    def get(self):
        self.render('createauthor.html',title = 'Create Author')
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password').encode('utf8')
        author = dao.findUserNameReturnPassWord(username)
        if not author:
            uid = random.randint(10, 100)
            has = bcrypt.hashpw(password,bcrypt.gensalt())
            screenName = str(username)
            dao.addAuthor(uid,username,has,screenName)
            self.write("Author Added \n SignIn")
            self.render('user/signin.html',title = 'Login',err="Author Added")
            return
        else:
            self.write("User Already Exist")
            self.render('createauthor.html',title = 'Create Author',err="Already Exist")
