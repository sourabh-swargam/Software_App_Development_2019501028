from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tqdm import tqdm
import os
import csv



engine = create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base()

class Book(Base):
	__tablename__ = "Books"
	isbn = Column(String, primary_key = True)
	title = Column(String)
	author = Column(String)
	year = Column(Integer)

Base.metadata.create_all(engine)
books_data = open('books.csv')
books_data = list(csv.reader(books_data))
# print(type(books_data), books_data)
for row in books_data[1:]:
	# print(row[1], type(row[1]))
	book = Book(isbn = row[0], title = row[1], author = row[2], year = int(row[3]))
	session.add(book)
print('Added')
session.commit()

