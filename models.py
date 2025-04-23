from sqlalchemy import Column, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class NewsArticle(Base):
    __tablename__ = "articles"

          
    title = Column(Text, nullable=False)
    summary = Column(Text)
    link = Column(String, primary_key=True) 
