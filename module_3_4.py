# Задача "Однокоренные":

# Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words
def single_root_words(root_word, *other_words):
    same_words = list() # Создайте внутри функции пустой список same_words, который пополнится нужными словами.
    root_word = root_word.lower() # Опустить регистр для базовой строки

    # При помощи цикла for переберите предполагаемо подходящие слова.
    for word in other_words:
        word = word.lower() # Опустить регистр для строки из кортежа

        if word.find(root_word) > -1 or root_word.find(word) > -1: # Пропишите корректное относительно задачи условие
            same_words.append(word) # , при котором добавляются слова в результирующий список same_words.

    return same_words # После цикла верните образованный функцией список same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)