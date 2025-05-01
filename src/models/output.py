from pydantic import BaseModel

class Article(BaseModel):
    headline: str
    summary: str

class Topic(BaseModel):
    topic: str
    articles: list[Article]

class SummaryOutput(BaseModel):
    date: str
    summary: str
    top_story: Article
    other_top_stories: list[Article]
    topics: list[Topic]

