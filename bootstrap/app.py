from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    books = [
        {'name': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'cover': 'https://m.media-amazon.com/images/M/MV5BMTkxNTk1ODcxNl5BMl5BanBnXkFtZTcwMDI1OTMzOQ@@._V1_.jpg'},
        {'name': 'Jane Eyre', 'author': 'Charlotte Brontë', 'cover': 'https://m.media-amazon.com/images/I/91zU70Aw9IS.jpg'},
        {'name': 'Anna Karenina', 'author': 'Leo Tolstoy', 'cover': 'https://m.media-amazon.com/images/M/MV5BMTU0NDgxNDg0NV5BMl5BanBnXkFtZTcwMjE4MzkwOA@@._V1_.jpg'}
    ]
    
    return render_template('index.html', books=books)

app.run(debug=True)