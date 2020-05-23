mysql
	database = "blog"
	user = "root"
	pass = ""
	port = "3306"
blog.conf
current = (blog.sql)
	
python
	virtualenv venv
	venv\Scripts\activate
	pip install -r requirements.txt
	python run.py