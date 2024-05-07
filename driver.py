"""
implementation of Book data store with cache
🙎🏻‍-→ GET Book -→ 🔋--ifNotFoundGetFromDB & Update cache-→ 💾

read through cache
write aside cache (store only in disk & bring in redis iff GET request & not found)
hence possibility of inconsistency
uses sqlite to store Book
"""
import json

from model import Book
from service import addBooks, getAllBooks, getBook
from flask import Flask, jsonify, Response
from http import HTTPStatus

app = Flask(__name__)


@app.route("/book", methods=['POST'])
def setBook():
    book1 = Book(title='Harry Potter', author='J.K Rowling')
    book2 = Book(title='Alchemist', author='Anna K')

    addBooks([book1, book2])
    return Response('Insert Ok', status=HTTPStatus.OK)


@app.route("/book", methods=['GET'])
def getAllBook():
    return jsonify(getAllBooks())


@app.route("/book/cache", methods=['GET'])
def getBookReadThroughCache():
    book1 = getBook(1)
    book2 = getBook(2)
    book3 = getBook(1)
    return jsonify([book1, book2, book3])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000, debug=True)  # uncomment if running from Docker and ↓ (so that we can access from postman/browser)
    # app.run(port=5000, debug=True)  # comment this if running from Docker and ^
