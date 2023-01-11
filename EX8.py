import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
parsed_response_text = response.json()
print(parsed_response_text)
token_value = parsed_response_text['token']
print(token_value)
time_seconds = parsed_response_text['seconds']
print(time_seconds)

response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=parsed_response_text)
print(response1.text)


time.sleep(time_seconds)


response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=parsed_response_text)
print(response2.text)