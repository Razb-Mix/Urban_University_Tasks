import unittest

# Скачайте исходный код для тестов.
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


# Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest.
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        instance_1 = Runner("Forest Gump") # создаётся объект класса Runner с произвольным именем.
        for i in range (10): instance_1.walk() # вызовите метод walk у этого объекта 10 раз.

        # методом assertEqual сравните distance этого объекта со значением 50.
        unittest.TestCase.assertEqual(self, instance_1.distance, 50)

    def test_run(self):
        instance_2 = Runner("Usain Bolt")  # создаётся объект класса Runner с произвольным именем.
        for i in range (10): instance_2.run() # вызовите метод run у этого объекта 10 раз.

        # методом assertEqual сравните distance этого объекта со значением 100.
        unittest.TestCase.assertEqual(self, instance_2.distance, 100)

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

# Запустите кейс RunnerTest.
if __name__ == "__main__":
    unittest.main()