import requests
import json
import os

def call_nyt_api(date):
    try:
        api_key = os.environ.get("NYT_API_KEY")
        
        if(api_key == None):
            raise Exception("Api Key Not Present")

        endpoint = "https://api.nytimes.com/svc/archive/v1" + f"/{date.year}" + f"/{date.month}" + ".json" + f"?api-key={api_key}"
        response = requests.get(endpoint, headers={"Accept": "application/json"})

        if response.status_code == requests.codes.ok:
            res = json.loads(response.text)  # < creates a dictionary
            return res['response']
        else:
            raise Exception(response.text)

    except Exception as e:
        print(e)
        raise Exception(e)