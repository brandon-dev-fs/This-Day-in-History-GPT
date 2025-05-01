from dotenv import load_dotenv

from module_articles.get_articles import get_articles
from module_files.write_file import write_summaries_file
from module_genai.anthropic.claude_token_count import claude_token_count
from module_genai.anthropic.cluade_get_summary import claude_get_summary
from module_genai.openai.openai_get_summary import openai_get_summary
from module_genai.model_prompt import model_prompt
from modules_dates.get_date import get_date

def main():
    load_dotenv(override=True)
    date = get_date()
    # Output is in Json format
    model = model_prompt()
    try:
        output = get_articles(date)
        if(len(output) > 0):
            summary = ""
            match model:
                case 1:
                    summary = openai_get_summary(output)
                case 2:
                    # claude_token_count(output) for testing purposes
                    summary = claude_get_summary(output)
                case _:
                    raise Exception("No Models Chosen")
            print("Summary generated...")
            write_summaries_file(summary, date)
        else:
            raise Exception("Unable to get articles")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()