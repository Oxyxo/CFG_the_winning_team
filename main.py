import requests
import json

#user input

response_API = requests.get(https://api.themoviedb.org/3/configuration?api_key=<<api_key>>)

data = response_API.text
parse_json = json.loads(data)
active_case = parse_json[#user_input?][]
