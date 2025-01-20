import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    # Метод для решения проблемы
    def sort_participants(self):
        # Создаём массив "скорость = бегун"
        dict_speed_runners = {self.participants[x].speed: self.participants[x] for x in range(len(self.participants))}
        # Вытаскиваем ключи-скорости из массива
        list_of_speed = list(dict_speed_runners.keys())
        # Сортируем список скоростей бегунов по убыванию, чтобы имитировать очередность прохождения дистанции
        list_of_speed.sort(reverse=True)
        # Создаём новый список бегунов с учётом сортировки по скорости
        sorted_participants = []
        for runner_speed in list_of_speed:
            # Записываем бегунов в список по отсортированному ключу-скорости
            sorted_participants.append(dict_speed_runners[runner_speed])
        else:
            # после выполнения цикла перезаписываем атрибут объекта отсортированным списком бегунов
            self.participants = sorted_participants

    def start(self):
        finishers = {}
        place = 1
        self.sort_participants() # определяем очередность прохождения дистанции согласно скорости бегунов
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


# Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest.
class RunnerTest(unittest.TestCase):
    # Класс RunnerTest дополнить атрибутом is_frozen = False
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        instance_1 = Runner("Forest Gump") # создаётся объект класса Runner с произвольным именем.
        for i in range (10): instance_1.walk() # вызовите метод walk у этого объекта 10 раз.

        # методом assertEqual сравните distance этого объекта со значением 50.
        unittest.TestCase.assertEqual(self, instance_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        instance_2 = Runner("Usain Bolt")  # создаётся объект класса Runner с произвольным именем.
        for i in range (10): instance_2.run() # вызовите метод run у этого объекта 10 раз.

        # методом assertEqual сравните distance этого объекта со значением 100.
        unittest.TestCase.assertEqual(self, instance_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        # создаются 2 объекта класса Runner с произвольными именами.
        instance_3 = Runner("Wolf")
        instance_4 = Runner("Fox")

        # 10 раз у объектов вызываются методы run и walk соответственно.
        for i in range (10):
            instance_3.walk()
            instance_4.run()

        # Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
        unittest.TestCase.assertNotEqual(self, instance_3.distance, instance_4.distance)




# Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:
class TournamentTest(unittest.TestCase):
    # Класс TournamentTest дополнить атрибутом is_frozen = True.
    is_frozen = True
    list_of_runners = ()
    @classmethod
    def setUpClass(cls):
        cls.all_results = {} # Это словарь в который будут сохраняться результаты всех тестов.

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        # где создаются 3 объекта:
        runner_Us = Runner("Усэйн", 10) # Бегун по имени Усэйн, со скоростью 10.
        runner_An = Runner("Андрей", 9)  # Бегун по имени Андрей, со скоростью 9.
        runner_Ni = Runner("Ник", 3) # Бегун по имени Ник, со скоростью 3.
        self.list_of_runners = (runner_Us, runner_An, runner_Ni)

    @classmethod
    def tearDownClass(cls):
        # выводятся all_results по очереди в столбец.
        for key, item in cls.all_results.items():
            for key_in, item in cls.all_results[key].items():
                cls.all_results[key][key_in] = cls.all_results[key][key_in].name
            print(cls.all_results[key])

    # Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90.
    # Усэйн и Ник
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament_1(self):
        # создаётся объект Tournament на дистанцию 90.
        tournament_1 = Tournament(90, self.list_of_runners[0], self.list_of_runners[2])
        # У объекта класса Tournament запускается метод start
        self.all_results['test1'] = (tournament_1.start())
        # В конце вызывается метод assertTrue
        unittest.TestCase.assertTrue(self.all_results['test1'][2], "Ник")

    # Андрей и Ник
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament_2(self):
        # создаётся объект Tournament на дистанцию 90.
        tournament_2 = Tournament(90, self.list_of_runners[1], self.list_of_runners[2])
        # У объекта класса Tournament запускается метод start
        self.all_results['test2'] = (tournament_2.start())
        # В конце вызывается метод assertTrue
        unittest.TestCase.assertTrue(self.all_results['test2'][2], "Ник")

    # Усэйн, Андрей и Ник.
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tournament_3(self):
        # создаётся объект Tournament на дистанцию 90.
        tournament_3 = Tournament(90, self.list_of_runners[0], self.list_of_runners[1], self.list_of_runners[2])
        # У объекта класса Tournament запускается метод start
        self.all_results['test3'] = (tournament_3.start())
        # В конце вызывается метод assertTrue
        unittest.TestCase.assertTrue(self.all_results['test3'][3], "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_max_speed(self):
        # При создании забега специально ставим участников не от самого быстрого к самому медленному.
        tournament_4 = Tournament(90, self.list_of_runners[1], self.list_of_runners[0], self.list_of_runners[2])
        # У объекта класса Tournament запускается метод start
        result = tournament_4.start()
        # Определяем скорость самого быстрого бегуна.
        max_speed = max(self.list_of_runners[0].speed, self.list_of_runners[1].speed, self.list_of_runners[2].speed)
        # Самый быстрый бегун должен получить первое место.
        unittest.TestCase.assertEqual(self, result[1].speed, max_speed, 'Выиграл забег не самый быстрый бегун!')


# Запустите кейс.
if __name__ == "__main__":
    unittest.main()