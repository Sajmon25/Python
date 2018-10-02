from flask import Flask, jsonify, request, Response, json

app = Flask(__name__)

books = [
    {
        'name': 'Green Egg and Ham',
        'price': 7.99,
        'isbn': 1564315496
    },
    {
        'name': 'The Cat In The Hat',
        'price': 6.99,
        'isbn': 5766531035
    },
]

__name__ == "__main__"
print(__name__)


# GET /books
@app.route('/books')
def get_books():
    return jsonify({'books': books})


def validBookObject(bookObject):
    if "name" in bookObject and "price" in bookObject and "isbn" in bookObject:
        return True
    else:
        return False


@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if validBookObject(request_data):
        new_book = {
            "name": request_data['name'],
            "price": request_data['price'],
            "isbn": request_data['isbn']
        }
        books.insert(0, new_book)
        response = Response("", 201, mimetype="application/json")
        response.headers['Location'] = "/books/" + str(new_book['isbn'])
        return response
    else:
        invalidBookObjectErrorMsg = {
            "error": "error",
            "helpString": "helpString"
        }
        response = Response(json.dumps(invalidBookObjectErrorMsg), status=400, mimetype="application/json")
        return response


# GET /books/isbn
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book["isbn"] == isbn:
            return_value = {
                'name': book["name"],
                'price': book["price"]
            }
    return jsonify(return_value)


# PUT
@app.route('/books/<int:isbn>', methods=['PUT'])
def replace_book(isbn):
    pass


app.run(port=5000)