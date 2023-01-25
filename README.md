# Flask Basics

Flask (FLex Advanced Security Kurl) is a micro web framework written in Python, initially released on 1st April 2010. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

Website: https://flask.palletsprojects.com/en/2.2.x/

## Installation and Usage

- the python package `virtualenvwrapper-win` can be used to create virtual environments for the project
- open command window in main folder and execute `mkvirtualenv [environment_name]`
- if the created virtual environment is not automatially opened use command `workon [environment_name]`
- in windows, the `lsvirtualenv` command can be used to get list of virtual environments in system

- install django using `pip install flask`

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
    return render_template('index.html')
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

### Base Template

- this base framework can be implimented to all other pages as needed
- the html pages where the same basic format is required, will be extended from this base template
- first create a base template html file (eg: base.html)
- use placeholders to specify where other blocks/contents will be placed

```
<!DOCTYPE html>
	<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Flask</title>

		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
	</head>
	<body>
		{% block body %}
		{% endblock %}
	</body>
</html>
```

- extend this template in all the new HTML files where this same base format is required

```
{% extends 'base.html' %}
{% block body %}
    <h1>Heading</h1>
    <!-- all elements as required -->
{% endblock %}
```

### Importing HTML

Section of template can be created separately and then later combined using include. That is `{% include 'section.html' %}`. Given below is an exmaple of the same.

```
<!-- base.html -->

<!DOCTYPE html>
	<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Flask</title>

		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
	</head>
	<body>
		{% include 'nav.html' %}
		
		{% block body %}
		{% endblock %}
	</body>
</html>
```

```
<1-- nav.html -->

<nav>
    <ul>
        <li>Home</li>
        <li>Contact</li>
    </ul>
</nav>
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

## Jinja

Jinja is a web template engine for the Python programming language. It was created by Armin Ronacher and is licensed under a BSD License. Jinja is similar to the Django template engine but provides Python-like expressions while ensuring that the templates are evaluated in a sandbox.

### Placing values

- to simple place a value, mention the variable name within double curly brackets

```
<!DOCTYPE html>
<html>
	<head>
		<title>Test</title>
	</head>
	<body>
		<h2>This is a template page - {{ name }}</h2>
	</body>
</html>
```

### Conditional

As Jinja allows Python-like expressions to be evaluated in the template, it can be used to make conditional decisions.

```
from flask import render_template

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name, isActive=True)
```

```
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Test</title>
	</head>
	<body>
		{% if isActive %}
			<h2>Name - {{ name }}</h2>
		{% else %}
			<h2>Name not provided</h2>
		{% endif %}
	</body>
</html>
```

### Looping

Iterable objects can also be looped through to display as required.

```
from flask import render_template

@app.route('/hello')
def hello():
	names = ['name1', 'name2', 'name3']
    return render_template('index.html', names=names)
```

```
<ul>
	{% for i in names %}
		<li>{{ i }}</li>
	{% endfor %}
</ul>
```

### Object Rendering

The main object is iterated through and then evaluated as needed.

```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    books = [
        {'name': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'cover': 'https://...._V1_.jpg'},
        {'name': 'Jane Eyre', 'author': 'Charlotte Brontë', 'cover': 'https://...U70Aw9IS.jpg'},
        {'name': 'Anna Karenina', 'author': 'Leo Tolstoy', 'cover': 'https://...MzkwOA._V1_.jpg'}
    ]
    
    return render_template('index.html', books=books)

app.run(debug=True)
```

```
<!DOCTYPE html>
	<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Templates</title>
	</head>
	<body>
		<h3>Books</h3>
		<ul>
			{% for book in books %}
				<div>
					<h2>{{ book.name }}</h2>
					<h4>{{ book.author }}</h4>
					<img src="{{ book.cover }}" width="200px">
				</div>
			{% endfor %}
		</ul>
	</body>
</html>
```

## Static Files

These are fixed cotent files such as css, js and such. They are placed in a separate folder named as `static` just as in the case of templates. But the linking of files is done in Jinja url format.

```
// main.css file in static folder

p {
	color: red;
}
```

```
<!-- in HTML template file -->

<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='main.css') }}">
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
| 1 | Dynamic template | [Go to code](https://github.com/jothomas1996/flask_basics/tree/main/basic_template) |
| 2 | Conditionals in template | [Go to code](https://github.com/jothomas1996/flask_basics/tree/main/conditional) |
| 3 | Looping in template | [Go to code](https://github.com/jothomas1996/flask_basics/tree/main/looping) |
| 4 | Object Rendering | [Go to code](https://github.com/jothomas1996/flask_basics/tree/main/object_rendering) |
| 5 | Bootstrap | [Go to code](https://github.com/jothomas1996/flask_basics/tree/main/bootstrap) |
| 6 | Static Files | [Go to code](https://github.com/jothomas1996/flask_basics/tree/main/static_files) |