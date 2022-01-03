import requests

payload_get = {"user": "name"}
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload_get)
print(response.text)

payload_post = {"user1": "name1"}
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload_post)
print(response.text)

payload_put = {"user2": "name2"}
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload_put)
print(response.text)

payload_delete = {"user3": "name3"}
response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload_delete)
print(response.text)

