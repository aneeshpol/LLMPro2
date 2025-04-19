import feedparser
import json
from pydantic import BaseModel, HttpUrl
from datetime import datetime
from dateutil import parser as dateparser
from typing import List, Optional

class NewsItem(BaseModel):
    title: str
    link: HttpUrl
    summary: str
    #date: datetime

def parser(rss_url):
    feed = feedparser.parse(rss_url)
    articles: List[NewsItem] = []
    for entry in feed.entries:
        
        try:
            article = NewsItem(
                    title= entry.get("title", "No Title"),
                    link= entry.get("link", ""),
                    summary= entry.get("summary", "No Summary"),
                    #published= dateparser.parse(entry.published)
                )
            articles.append(article)
        except Exception as e:
            print(f"Skipping invalid entry: {e}")

    return articles




