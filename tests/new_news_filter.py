"""uses the news api to get news notifications"""

import json
import requests

def get_news() -> list:
    """Uses the news api to get news article

    returns a list of dictionaries containg each article"""

    #opening the config file
    with open("config.json", 'r') as f:
        json_file = json.load(f)

    #getting the components to construct the url
    news_section = json_file["news"]
    news_key = news_section["api-key"]
    base_url = news_section["base_url"]
    country = news_section["country"]

    complete_url = base_url + "country=" + country + "&apiKey=" + news_key

    #making the restful api call
    response = requests.get(complete_url)
    news_dict = response.json()

    return news_dict



if __name__ == "__main__":
    print(get_news())
