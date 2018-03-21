from flask import Flask, render_template

app = Flask(__name__)

counts=0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('index.html')
    global counts
    counts += 1
