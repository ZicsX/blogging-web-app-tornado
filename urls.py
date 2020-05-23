from action.index import Index
from action.article import Article
from action.signin import Signin
from action.publish import Publish
from action.signout import Signout
from action.page import About,Type
from action.api import Article as ART,Comment as com
from action.archive import Archive
from action.createuser import AuthCreateHandler
urls = [
	(r'/', Index),
	(r'/article/([^\n]*)',Article),
	(r'/signin',Signin),
	(r'/publish',Publish),
	(r'/api/article/([^\n]*)',ART),
	(r'/api/comment',com),
	(r'/signout',Signout),
	(r'/about',About),
	(r'/type',Type),
    (r'/archive',Archive),
    (r"/auth/create", AuthCreateHandler)
]