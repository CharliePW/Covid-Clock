"""this module contains a function that gets covid data """

import requests
import json

def get_data() -> dict :
    """Uses the gov.uk covid19 api to get covid data from a certain area

    return the latest new covid cases"""

    #opening the config file
    with open("config.json", 'r') as f:
        json_file = json.load(f)

    #getting the components to construct the url
    covid_section = json_file["covid"]
    base_url = covid_section["base_url"]
    city = covid_section["city"]
    filters = "filters=areaName=" + city
    structure = '&structure={"date":"date","newCases":"newCasesByPublishDate"}'

    complete_url = base_url + filters + structure

    response = requests.get(complete_url)

    #logs if there is an error
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        logging.error(f'Request failed: { response.text }')

    #making the restful api call
    x = response.json()
    covid_dict = {"title":"Latest covid data in your area","content":""}
    covid_data = x["data"]
    covid_dict.update({"content": str(covid_data[0]["newCases"]) + " new cases"})

    return covid_dict

if __name__ == "__main__":
    print(get_data())
