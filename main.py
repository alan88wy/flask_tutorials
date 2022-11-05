import os
from flask import Flask
from flask import request
from flask import render_template # Template for rendering

class Config(object):
    MESSAGE = os.environ.get("MESSAGE")

app = Flask(__name__)
app.config.from_object(Config)

# Static files
# By default, 
# Flask serves up static files from the "static" folder.

# Asynchronous Tasks
# @app.route("/")
# async def home():
#    result = await some_async_task()
#    return resule

# Middleware

# class middleware:
#     def __init__(self, app) -> None:
#         self.app = app

#     def __call__(self, environ, start_response):
#         start = time.time()
#         response = self.app(environ, start_response)
#         end = time.time() - start
#         print(f"request processed in {end} s")
#         return response

# app = Flask(__name__)
# app.wsgi_app = middleware(app.wsgi_app)

# end of Middleware

# CORS
# pip install flask-cors

# Basic implementation:

# from flask_cors import CORS

# app = Flask(__name__)

# CORS(app)

# End of CORS



@app.route("/", methods=['GET', 'POST'])
def home():
    # handle POST
    if request.methods == "POST":
        return {"Hello": "POST"}
    
    # handle GET
    return {"Hello", "GET"}

@app.route("/settings")
def get_settings():
    return { "message": app.config["MESSAGE"] }

# Url parameters
@app.route("/employee/<int:id>")
def home():
    return {"id": id}

# Query Parameters
@app.route("/employee")
def home():
    department = request.args.get("department")
    return {"department" : department}

# Templates

@app.route("/about")
def home():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()