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

    articles = news_dict["articles"]
    news_list = []

    #making a dictionary out of each article
    for article in articles:

        new_dict = {
            "title":"",
            "content":"",
        }

        title = str(article["title"])
        content = str(article["url"])


        new_dict.update({"title": title})
        new_dict.update({"content": content})

        news_list.append(new_dict)

        #this was used for filtering for articles mentioning covid-19
        """covid_words = ["lockdown","covid","quarantine","symptons","pandemic","coronavirus",
        "virus","covid-19"]"""

        """for word in covid_words:
            if word in content or word in title:
                new_dict.update({"title": article["title"]})
                new_dict.update({"content": article["url"]})
                news_list.append(new_dict)
                break"""

    return news_list

if __name__ == "__main__":
    print(get_news())
