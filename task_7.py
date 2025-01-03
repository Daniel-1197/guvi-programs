# 1. Using the URL "https://restcountries.com/v3.1/all" write python code
import requests
import json

class Get_input:
    def __init__(self,url):
        self.url = url

    def fetch_data(self):
     page_req = requests.get(self.url)
     parsed_json = page_req.json()
     return parsed_json

    def display(self):
        fetched_data = self.fetch_data()
        for i in fetched_data:
            country = i['name']['common']
            print(f'The country name is {country}')
            try:
                for k,l in i['currencies'].items():
                    print(f"The currency name is {l['name']}")
                    print(f"The symbol is {l['symbol']}")
            except Exception as e:
                print(e)

    def dollar_countries(self):
        fetched_data = self.fetch_data()
        for i in fetched_data:
            try:
              for k,l in i['currencies'].items():
                if l['symbol'] == '$':
                        print(i['name']['common'])
            except Exception as e:
                print(e)

    def euro_countries(self):
        fetched_data = self.fetch_data()
        for i in fetched_data:
            try:
                for k,l in i['currencies'].items():
                    if l['symbol'] == '€':
                        print(i['name']['common'])
            except Exception as e:
                print(e)


Get_url_data = Get_input("https://restcountries.com/v3.1/all")
Get_url_data.display()
Get_url_data.dollar_countries()
Get_url_data.euro_countries()

# 2. Using the URL "https://api.openbrewerydb.org/v1/breweries" write python code

def all_breweries(a):
    get_data = requests.get(a)
    parsed_data = get_data.json()
    new_york_breweries = []
    alaska_breweries = []
    maine_breweries = []
    for i in parsed_data:
        if i["state"] == "New York" or i["state"] == "Alaska" or i["state"] == "Maine":
            print(i.get("name","None"))
        if i['state'] == 'New York':
            new_york_breweries.append(i.get("name","None"))
        if i['state'] == 'Alaska':
            alaska_breweries.append(i.get("name",None))
        if i['state'] == 'Maine':
            maine_breweries.append(i.get("name",None))
    print(f"No. of breweries in New York :{len(new_york_breweries)}")
    print(f"No. of breweries in  Alaska :{len(alaska_breweries)}")
    print(f"No. of breweries in Maine :{len(maine_breweries)}")


display_breweries = all_breweries("https://api.openbrewerydb.org/v1/breweries")

