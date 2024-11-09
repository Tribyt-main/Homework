import unittest
import logging
from Module_12.Module_12_4.rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class TestRunner(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Ок')
    def test_walk(self):
        try:
            first = Runner('Nik', speed=-10)
            first.distance = 0
            for i in range(0, 10):
                first.walk()
            logging.info('test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner')

    def test_run(self):
        try:
            first = Runner(111, speed=10)
            first.distance = 0
            for i in range(0, 10):
                first.run()
            logging.info('test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')


if __name__ == '__main__':
    unittest.main()
