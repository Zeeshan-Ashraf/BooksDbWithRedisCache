# BooksDbWithRedisCache
CRUD application in python using SqlAlchemy &amp; Sqlite DB / MySql with performance improvement using Redis cache running in docker (or local)

# Install & Run
install docker from Docker website [Download](https://docs.docker.com/engine/install/)

`cd docker`

`docker-compose up`

shut down command `docker-compose down`

# verify app by calling API

`POST 127.0.0.1:6000/book`

`GET 127.0.0.1:6000/book`

`GET 127.0.0.1:6000/book/cache`
