import json
from model import Book, session
import redis

redisClient = redis.Redis(host='localhost', port=6379)


def addBooks(books: list[Book]) -> None:
    try:
        session.add_all(books)
        session.flush()
        session.commit()
        session.close()
    except Exception as e:
        session.rollback()
        raise e


def getAllBooks() -> list[Book]:
    return session.query(Book).all()


def getBook(id: int):
    book = getBookFromCache(id)
    if book:
        print("found in cache")
        return book
    print("didn't found in cache, getting from db")
    book = session.get(Book, id)
    if book:
        setBookToCache(book)
    return book


def getBookFromCache(id: int):
    print("getting book from cahche")
    return redisClient.get(str(id))


def setBookToCache(book: Book):
    print("setting book in cache")
    return redisClient.set(str(book.id), json.dumps(book.toJson()))
