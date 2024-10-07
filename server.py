from flask import Flask, render_template
import os

os.environ["DATABASE_URL"]


app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)