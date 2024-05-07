from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from dataclasses import dataclass

# CONNECT_DB_URI = 'sqlite:///data.db'
CONNECT_DB_URI = MYSQL_DB_CONNECT_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format("root","","host.docker.internal","3306","data_db")  # uncomment this if running via docker-compose
# CONNECT_DB_URI = MYSQL_DB_CONNECT_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format("root","","127.0.0.1","3306","data_db") # comment this & uncomment above if running from docker ^

engine = create_engine(CONNECT_DB_URI)
session = sessionmaker(bind=engine)()
Base = declarative_base()


@dataclass
class Book(Base):
    __tablename__ = 'book'
    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(255))
    author: str = Column(String(255))

    def toJson(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Base.metadata.create_all(engine)
