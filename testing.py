import pytest
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "OK"}

def test_hello():
    res = app.test_client().get("/")

    assert res.status_code == 200
    assert res.data == b'{"message":"OK"}\n'