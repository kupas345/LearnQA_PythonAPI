import requests

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True, headers=headers)
first_response = response.history[0]
print(f'Первый url {first_response.url}')

second_response = response.history[1]
print(f'Второй url {second_response.url}')

tretiy_response = response.history[2]
print(f'Третий url {tretiy_response.url}')

