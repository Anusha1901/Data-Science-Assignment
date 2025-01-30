from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Review(Base):
    __tablename__ = 'imdb_reviews'
    
    id = Column(Integer, primary_key=True)
    review_text = Column(Text)
    sentiment = Column(String(10))

def init_db():
    engine = create_engine('sqlite:///reviews.db')
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()
