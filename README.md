# Basic Web App for blogging
This blogging app build in Tornado Web Server.
### Dependencies
#### Python | Tornado

##### Application Dependencies
```
tornado
mysql
mysql-connector-python
markdown2
bcrypt
configparser
```
#### Local development
Running the application locally

###### Virtual Enviornment
Create python virtual environment
```bash
python -m virtualenv env
source env/bin/activate
```
>**Note** - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:
```bash
env/Scripts/activate
```
##### Install Dependencies

Install application dependencies within the `requirements.txt` file using pip:
```bash
pip install -r requirements.txt
```

##### Database Setup
Create database to store data
With Mysql running, restore a database using the blog.sql file. 
and update blog.conf file with database, user, pass and port
#### Running the server locally
To run the server, execute:
```bash
python run.py
```
