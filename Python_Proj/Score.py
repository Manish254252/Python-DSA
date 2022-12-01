import requests
from pprint import PrettyPrinter

printer = PrettyPrinter()

url = "https://weatherapi-com.p.rapidapi.com/sports.json"

querystring = {"q": "London"}

headers = {
    "X-RapidAPI-Key": "USE API KEY",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request(
    "GET", url, headers=headers, params=querystring).json()
if 'football' in response.keys():
    for i in response:
        print(i)
        c = i['country']
        t = i['tournament']
        stad = i['stadium']
        st = i['start']
        print('--------------------------------------')
        print(f"{c}--{t}--{stad}--{st}")

print(type(response))
print(response)
