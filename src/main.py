from module_articles.get_articles import getArticles
from dotenv import load_dotenv

def main():
    load_dotenv()
    news_desk = ["Financial Desk"]

    year = 0
    while not (year > 1851 and year < 2019):
        year = int(input("Enter a year (1851-2019): "))
    month = 0
    while not (month > 1 and month < 12):
        month = int(input("Enter a month (1-12): "))
    desk_num = 0
    desk = news_desk[desk_num]


    # Output is in Json format
    try:
        output = getArticles(year, month, desk)
        print(str(output))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()