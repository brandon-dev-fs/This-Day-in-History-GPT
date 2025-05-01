from datetime import date

def filter_articles(articles, day):
    print("Filtering articles...")
    relevant_sections = [
        "Archives",
        "Business Day",
        "Education",
        "Health",
        "Science",
        "Sports",
        "Technology",
        "U.S.",
        "World"
    ]

    articles_list = articles["docs"]
    news = []

    for article in articles_list:
        pub_date = date.fromisoformat(article["pub_date"].split('T')[0])

        if article["section_name"] in relevant_sections and article["document_type"] == "article" and not article["abstract"] == "" and pub_date.day == day:
            news_article = {
                "Headline": article["headline"]["main"],
                "Summary": article["abstract"],
                #"Url": article["web_url"]
            }
            news.append(news_article)
    
    print(f"Found {len(news)} articles")

    return news