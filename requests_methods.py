import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)

response = requests.options("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)

response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {'method': 'POST'})
print(response.text)

response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {'method': 'GET'})
print(response.text)







