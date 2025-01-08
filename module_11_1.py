import requests
from PIL import Image
from io import BytesIO

"------------------------------Библиотека Requests-------------------------------------------------------------------"
def get_info_API(file_name: str):
    with open(file_name, 'w', encoding= 'utf-8') as file:
        file.write(r.text)

# - запросить данные с сайта и вывести их в консоль.
r = requests.get('https://api.github.com')
print(r.text)

# Доп. задание из примечания
print("Код состояния ответа сервера:", r.status_code)
print(r.headers['content-type']) # Вывести заголовки
print(r.encoding) # Вывести кодировку
name_of_file = "content" # имя для файла с результатом запроса GET
get_info_API(name_of_file) # записать результат запроса GET в файл

"------------------------------Библиотека Pillow-------------------------------------------------------------------"

response = requests.get('https://httpbin.org/image/jpeg') # Скачиваем картинку
image = Image.open(BytesIO(response.content)) # Открываем картинку

# обработать изображение
image = image.crop((0, 0, 150, 178)) # Вырезаем область картинки
image = image.rotate(120, expand=True) # Меняем угол изображения
image = image.convert("L") # Конвертируем цвет у картинки
image.show() # Показываем результат
image.save("Picture.png") # сохранить в другой формат.