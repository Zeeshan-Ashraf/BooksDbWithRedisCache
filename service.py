import json
from model import Book, session
import redis

# redisClient = redis.Redis(host='localhost', port=6379, decode_responses=True)  # comment this if running from docker & uncomment next line ↓
redisClient = redis.Redis(host='host.docker.internal', port=6379, decode_responses=True)  # uncomment this if running from Docker & comment above line ↑
# if decode_responses not set then it'll return in binary coded string e.g b'"hello World" so use decode

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
    print("getting book from cache")
    return redisClient.get(str(id))


def setBookToCache(book: Book):
    print("setting book in cache")
    return redisClient.set(str(book.id), json.dumps(book.toJson()))
