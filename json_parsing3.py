##дом задание №5 - не получается отфильтровать по выводу только с 2 message, отправил вопрос в чат

import json

second_message = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(second_message)

for messages in obj:
    print(obj['messages'][1]['message'])






