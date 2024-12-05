# Задача "Записать и запомнить":

def custom_write(file_name: str, strings: list):
    file = open(file_name, 'a', encoding='utf-8')
    strings_positions: dict = {}
    num_of_row: int = 0
    for string_ in strings:
        num_of_row += 1
        strings_positions['{}, {}'.format(num_of_row, file.tell())] = string_
        file.write('%s\n' % string_) # Записывать в файл file_name все строки из списка strings, каждая на новой строке.
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
  print(elem)