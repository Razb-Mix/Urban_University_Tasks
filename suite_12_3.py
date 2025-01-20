# Задача "Заморозка кейсов":
import tests_12_3
import unittest

# Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной с произвольным названием.
set_of_tests = unittest.TestSuite()

# Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
set_of_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
set_of_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

# Создайте объект класса TextTestRunner, с аргументом verbosity=2.
runner = unittest.TextTestRunner(verbosity=2)
runner.run(set_of_tests)