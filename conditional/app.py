from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<username>')
def hello(username=None):
    isActive = False
    if username:
        isActive = True
    return render_template('index.html', username=username, isActive=isActive)

app.run(debug=True)