import requests

try:
	sites = str(input("Введи сайт: "))

	links = requests.get(f'https://{sites}')
	response = links.status_code
	print("Status: ", response)


	if response == 200:
		with open(f'{sites}.html', 'w', encoding='utf-8') as file:
			file.write(links.text)
			print(f'Страница {sites} сохранена')
	else:
		print("Попробуй другую страницу")
except:
	print("Произошла ошибка")
