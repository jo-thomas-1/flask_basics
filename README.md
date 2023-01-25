# Flask Basics

Flask (FLex Advanced Security Kurl) is a micro web framework written in Python, initially released on 1st April 2010. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

Website: https://flask.palletsprojects.com/en/2.2.x/

## Installation and Usage

- the python package `virtualenvwrapper-win` can be used to create virtual environments for the project
- open command window in main folder and execute `mkvirtualenv [environment_name]`
- if the created virtual environment is not automatially opened use command `workon [environment_name]`
- in windows, the `lsvirtualenv` command can be used to get list of virtual environments in system

- install django using `pip install flask`
- to get any specific version use `pip install django==[version]`

- in project folder create a python file `app.py`
- the projects code will be provided in this file

- to run the created application in flask, make sure to call the `run()` method on the flask class instance
- open the project folder in command window
- run the command `python app.py`
- once this command is executed, the url to the application will be displayed

## Basic Application

- first import the `flask` class. An instance of this class will be the WSGI application
- create an instance of this class. The first argument is the name of the application’s module or package. `__name__` is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files
- use the `route()` decorator to tell Flask what URL should trigger the function
- the function returns the message to be displayed in the browser

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()
```

WSGI (Web Server Gateway Interface) is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language.

- it is not compulsory to provide the file name as `app.py`
- the name provided for creating the flask class instance is the name used in route decorators

```
from flask import Flask

app_name = Flask(__name__)

@app_name.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app_name.run()
```

## Routing

- the route decorator is used to define new paths or bind functions to a url
- first the route is defined and then just below, the desired function is defined

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/new")
def new():
    return "<p>New Page</p>"

app.run()
```

## Templates

Templates are nothing but HTML files. These files are rendered in by Flask.

- the `render_template()` method is used for this
- it is imported from flask
- the name of template file and the values required by the tamplate are both passed as arguments to this function

```
from flask import render_template

@app.route('/hello/')
def hello():
    return render_template('index.html)
```

```
<!-- /templates/index.html -->

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Test</title>
	</head>
	<body>
		<h2>This is a template page</h2>
	</body>
</html>
```

- flask will look for templates in the templates folder
- if the application is a module, this folder is next to that module

	```
	/application.py
	/templates
	    /hello.html
	```

- if the application a package this folder is inside the package

	```
	/application
	    /__init__.py
	    /templates
	        /hello.html
	```


## Passing Values

These are various methods by which data can be moved around the application as required.

### Passing values in url

- to pass values through the url tags can be used when defining routes
- the variable name is defined in the route using arrow heads
- in order to be able to access this value, the same name also must be mentioned as an argument to the function
- for printing out these values placeholder characters are used
	- `%s` for string
	- `%d` for integer
- a converter can be used to specify the data type of the argument like `<converter:variable_name>`
- for example to get integer values, `@app.route("/home/<int:variable_name>")`
- available converters are,
	- string - (default) accepts any text without a slash
	- int - accepts positive integers
	- float - accepts positive floating point values
	- path - like string but also accepts slashes
	- uuid - accepts UUID strings

```
@app.route("/home/<variable_name>")
def hello_world(variable_name):
    return "<p>Hello, %s</p>" % variable_name
```

### Passing values to templates

- the `render_template()` method is used for redering templates
- the name of template file and the values required by the tamplate are both passed as arguments to this function
- once the values are passed, jinja placeholders are used to place the values in the template

```
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)
```

```
<!-- /templates/index.html -->

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Test</title>
	</head>
	<body>
		<h2>This is a template page - {{ name }}</h2>
	</body>
</html>
```

## Debug Mode

By enabling debug mode, the server will automatically reload if code changes, and will show an interactive debugger in the browser if an error occurs during a request. When turned off, in case of errors it just shows a message "Internal Server Error"

- the debug mode is `off` by default
- to trun it on, pass `debug=True` as an argument in the run command

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run(debug=True)
```

## Example Projects

The following are some sample projects created based on the above documentation.

| # | Name | Action |
|---|---|---|
| 1 |  | [Go to code]() |
