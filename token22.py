import requests
import time

response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params={"token":"wNwoTMyozMxASNw0SMw0iMyAjM"})
key1 = "status"

if key1 in response == "Job is ready":
    print("OK")

response2 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
key2 = "seconds"

if key2 in response == 42:
    print("Start : 0s" % time.ctime())
    time.sleep(42)
    print("End : 43s" % time.ctime())

response3 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params={"token":"wNwoTMyozMxASNw0SMw0iMyAjM"})

if {"result": "42", "status": "Job is ready"} in response3:
    print("Everything is allright")
