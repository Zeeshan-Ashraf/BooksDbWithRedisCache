from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from dataclasses import dataclass

SQLITE_CONNECT_DB_URI = 'sqlite:///data.db'
engine = create_engine(SQLITE_CONNECT_DB_URI)
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