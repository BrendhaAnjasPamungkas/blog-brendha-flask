# import aplikasi flask untuk dipakai di web kita
import os

from cs50 import SQL

from flask import Flask, flash, jsonify, redirect, render_template, request, session


# mengatur nama aplikasi
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/login")
def login():
    return 'halaman login'
