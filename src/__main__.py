from dotenv import load_dotenv

from module_articles.get_articles import get_articles
from module_files.write_file import write_summaries_file
from module_genai.claude_token_count import claude_token_count
from module_genai.cluade_get_summary import claude_get_summary
from modules_dates.get_date import get_date

def main():
    load_dotenv()
    date = get_date()
    # Output is in Json format
    try:
        output = get_articles(date)
        if(len(output) > 0):
            claude_token_count(output)
            summary = claude_get_summary(output)
            print("Summary generated...")
            write_summaries_file(summary, date)
        else:
            raise Exception("Unable to get articles")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()