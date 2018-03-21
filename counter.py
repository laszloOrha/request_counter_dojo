from flask import Flask, render_template, redirect

app = Flask(__name__)

counts = {"get":0, "post":0, "put":0, "delete":0}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    global counts
    counts += 1
    return redirect('/')

if __name__ == '__main__':
    app.secret_key = "topsecret"
    app.run(debug=True, host='0.0.0.0', port=5000)