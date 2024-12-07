# Задача "Найдёт везде":

class WordsFinder:
    def __init__(self, *names_of_files):
        # принимает при создании неограниченное количество названий файлов и записывает
        # их в атрибут file_names в виде списка или кортежа.
        self.file_names = names_of_files

    def get_all_words(self):
        all_words = {} # Создайте пустой словарь all_words.
        for name_of_file in self.file_names:
            # Переберите названия файлов и открывайте каждый из них, используя оператор with.
            with open(name_of_file,'r', encoding = 'utf-8') as file:
                text = file.read().lower() # Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).

                for sign in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    # Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено
                    # пробелами, это не дефис в слове).
                    text = text.replace(sign, "")

                # Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
                # В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.
                all_words[name_of_file] = text.split()
        return all_words

    def find(self, word):
        # где word - искомое слово. Возвращает словарь,
        # где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
        result_dict = {}
        for name, words in self.get_all_words().items(): # перебираем пары в словаре
            for element in words: # перебираем пары в словаре из значения текущей пары
                if word.lower() == element.lower(): # ищем первое совпадение в списке слов
                    result_dict[name] = words.index(word.lower()) + 1 # + 1, т.к. индексация в словаре начинается с нуля
                    break # выходим из цикла, т.к. нужна позиция первого такого слова в списке слов этого файла.
        return result_dict

    def count(self, word):
        # где word - искомое слово. Возвращает словарь,
        # где ключ - название файла, значение - количество слова word в списке слов этого файла.
        result_dict = {}
        for name, words in self.get_all_words().items(): # перебираем пары в словаре
            quantity_of_words = 0 # счётчик для подсчета количеств совпадений в текущей паре словаря
            for element in words: # перебираем пары в словаре из значения текущей пары
                if word.lower() == element.lower(): # ищем совпадения в списке слов
                    quantity_of_words += 1 # пинаем счётчик
            result_dict[name] = quantity_of_words # записываем результат обхода в словарь
        return result_dict
"------------------------------------------ Исполняемый код -----------------------------------------------------------"

finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
print()
print()
print()
# Поиск во всех стихотворениях
# Поисковое слово: 'the'
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                       'Rudyard Kipling - If.txt',
                       'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))