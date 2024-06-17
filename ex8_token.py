import time
import json

import requests

class Te:
    def new(self):
        x = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
        print(x.status_code)
        z = (x.text)
        return z

    def next(self):
        x = self.new()
        obj = json.loads(x)
        token = obj['token']
        sec = obj['seconds']
        return token, sec

t = Te()
z = t.next()

[a, b] = z
token = a
sec = b

y2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
y3 = y2.text
obj = json.loads(y3)
status = obj['status']

if status == "Job is NOT ready":
    print("Job is NOT ready. It's ok. Please be more patient, wait for a while")

time.sleep(sec)

y1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
y4 = y1.text
obj = json.loads(y4)
status2 = obj['status']

if status2 == "Job is ready":
    print("Job is ready. Great job, mister")
print(y1.text)
print(y1.status_code)
