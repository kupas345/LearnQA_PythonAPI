import requests

method = ["GET", "POST", "PUT", "DELETE"]

print("Часть I. Отправка без method")
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)


print("Часть II. http-запрос не из списка")

response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)

response = requests.options("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)

response = requests.patch("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)


print("Часть IV. Цикл")
for item in method:
    payload = {"method": item}

    print(f'Используем метод {item}')
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
    print(response.text)

    print(f'Используем метод {item}')
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(response.text)

    print(f'Используем метод {item}')
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(response.text)

    print(f'Используем метод {item}')
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(response.text)