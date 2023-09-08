# import aplikasi flask untuk dipakai di web kita
from flask import Flask


# mengatur nama aplikasi
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/login")
def login():
    return 'halaman login'