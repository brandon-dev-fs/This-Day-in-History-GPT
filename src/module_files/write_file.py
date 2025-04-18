import json
from pathlib import Path

from module_files.build_path import build_path

def write_articles_file(path, articles):
    file = open(path, "w")
    try:
        print("writing to " + str(path))
        to_write = json.dumps(articles, indent=2)
        file.write(to_write)
    except Exception as e:
        print(e)
    finally:
        file.close()

def write_summaries_file(summary, summary_date):
    path = build_path("summaries", summary_date)

    if(not Path(path).exists()):
        file = open(path, "w")
        try:
            print("writing to " + str(path))
            file.write(summary)
        except Exception as e:
            print(e)
        finally:
            file.close()