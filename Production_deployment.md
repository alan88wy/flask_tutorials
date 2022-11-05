# Production Server

Flask by default runs a development WSGI (Web Server Gateway Interface) application server. For production, you'll need to use a production-grade WSGI app server like Gunicorn, uWSGI, or mod_wsgi

Install Gunicorn:

pip install gunicorn

Start server:

# main.py
# app = Flask(__name__)

gunicorn main:app