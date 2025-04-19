from rss_parser import parser, NewsItem
from database import Session
from typing import List
from models import NewsArticle

def save_articles(news_items: List[NewsItem]) -> None:
    session = Session()
    saved_count = 0
    for item in news_items:
        try:
            article = NewsArticle(
                title=item.title,
                link=str(item.link),
                summary=item.summary,
               
            )
            session.merge(article)
            saved_count += 1
        except Exception as e:
            print(f"Failed to save article: {item.title[:50]} - {e}")

    session.commit()
    session.close()
    #print(f"Saved {saved_count} articles to the database.")

def ingest_rss(feed_url: str) -> None:
    print(f"\n Fetching RSS feed from: {feed_url}")
    news_items = parser(feed_url)
    print(f"Parsed {len(news_items)} articles.")
    
    if news_items:
        save_articles(news_items)
    else:
        print("No valid articles to save.")
