"""
implementation of Book data store with cache
🙎🏻‍-→ GET Book -→ 🔋--ifNotFoundGetFromDB & Update cache-→ 💾

read through cache
write aside cache (store only in disk & bring in redis iff GET request & not found)
hence possibility of inconsistency
uses sqlite to store Book
"""
from model import Book
from service import addBooks, getAllBooks, getBook

book1 = Book(title='Harry Potter', author='J.K Rowling')
book2 = Book(title='Alchemist', author='Anna K')

addBooks([book1, book2])

for book in getAllBooks():
    print(book.id, book.title, book.author)

book = getBook(1)
print(book)
book = getBook(1)
print(book)
book = getBook(2)
print(book)
