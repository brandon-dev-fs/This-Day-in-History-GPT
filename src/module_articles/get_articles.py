from pathlib import Path

from dotenv import load_dotenv

from module_articles.filter_articles import filter_articles
from module_files.build_path import build_path
from module_files.read_file import read_file
from module_files.write_file import write_articles_file
from module_nytimes_api.call_nyt_api import call_nyt_api

def get_articles(date):
    path = build_path("articles", date)
   
    if(Path(path).exists()):
        articles = read_file(path)
    else: 
        articles = call_nyt_api(date)
        write_articles_file(path, articles)
    
    print(type(articles))

    return filter_articles(articles, date.day)