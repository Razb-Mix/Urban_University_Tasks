# Дополнительное практическое задание по модулю: "Классы и объекты."
# Задание "Свой YouTube":
from time import sleep

class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return f'{self.nickname}, {str(self.password)}'

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname
        else:
            return f'Ошибка! "{other}" - неверный тип данных.'


class Video:
    def __init__(self, title: str, duration: int, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'{self.title}'

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        else:
            return f'Ошибка! "{other}" - неверный тип данных.'


class UrTube:

    def __init__(self):
        self.users = [] # список объектов User
        self.videos = [] # список объектов Video
        self.current_user = None # текущий пользователь, User

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if (nickname + ", " + str(hash(password))) == repr(user):
                self.current_user = user

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password: str, age: int):
        if len(self.users) == 0:
            self.users.append(User(nickname, password, age))
            self.current_user = self.users[0] # После регистрации, вход выполняется автоматически.
            return

        for i in range (len(self.users)):
            user_from_list = self.users[i] # Вытащить в переменную объект из списка
            if nickname == user_from_list.nickname: # Сравниваем nickname нового пользователя и уже зарегистрированного
                print(f"Пользователь {nickname} уже существует")
                return
            else:
                self.users.append(User(nickname, password, age)) # добавить пользователя в список
                self.current_user = self.users[len(self.users)-1] # После регистрации, вход выполняется автоматически.

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, search_word: str):
        search_word = search_word.lower()
        list_of_results = []
        for word in self.videos:
            if search_word in repr(word).lower():
                list_of_results.append(repr(word))
        return list_of_results

    def watch_video(self, title):
        if self.current_user is None: # Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for video in self.videos:
                if title == repr(video): # Нашили видео по названию
                    if video.adult_mode and self.current_user.age < 18: # Проверили возраст пользователя и наличие ограничения
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        break
                    else:
                        for video.time_now in range(1, video.duration + 1): # Показываем видос
                            sleep(1)
                            print(f"{video.time_now} ", end='')
                        print("Конец видео")
                        video.time_now = 0


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)