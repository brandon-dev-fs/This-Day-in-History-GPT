import requests
import json
import os
from dotenv import load_dotenv
from addFile import AddFile

load_dotenv()

httpEndpoint = "https://api.nytimes.com/svc/archive/v1"

api_key = os.environ.get("NYT_API_KEY")

if(api_key == None):
    exit

def getArticles(year, month, desk=None):
    requestUrl = httpEndpoint + f"/{year}" + f"/{month}" + ".json" + f"?api-key={api_key}"
    print(requestUrl)
    requestHeaders = {"Accept": "application/json"}
    try:
        response = requests.get(requestUrl, headers=requestHeaders)

        if response.status_code == requests.codes.ok:
            resJson = json.loads(response.text)  # < creates a dictionary
            data = FilterResults(resJson, desk)
            newPath = AddFile(month, year, json.dumps(data, indent=4))
            return f"article added at {newPath}"
        else:
            raise Exception(response.text)

    except Exception as e:
        print(e)
        raise Exception(e)


def FilterResults(json, desk):
    responseJson = json["response"]["docs"]

    if desk is not None:
        # j = responseJson["docs"]
        # if j["news_desk"] != desk:
        # responseJson["docs"].remove(j)
        for article in responseJson:
            print(article["headline"]["main"])
        #return filter(lambda j: j["news_desk"] == desk, responseJson["docs"])
