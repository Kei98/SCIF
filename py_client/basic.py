import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/"

get_reponse = requests.get(
    endpoint, json={"query": "Hello World!"})  # HTTP Request
print(get_reponse.text)  # print raw text response

#print(get_reponse.json())
print(get_reponse.status_code)
