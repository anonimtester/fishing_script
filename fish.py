import requests

sites = str(input("Введи сайт: "))

links = requests.get(f'https://{sites}')
response = links.status_code
print("Status: ", response)

if response == 200:
	with open(f'{sites}.html', 'w', encoding='utf-8') as file:
		file.write(links.text)
		print("Страница f'{sites}' сохранена")
else:
	print("Попробуй другую страницу")