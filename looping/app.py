from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    names = ['John', 'Peter', 'Nithi', 'Nayana']
    return render_template('index.html', names=names)

app.run(debug=True)