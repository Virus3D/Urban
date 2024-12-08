import logging
from rt_with_exceptions import Runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner1 = Runner('Runner1', -5)
            for _i in range(10):
                runner1.walk()
            self.assertEqual(runner1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.error('Неверная скорость для Runner')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner1 = Runner(50)
            for _i in range(10):
                runner1.run()
            self.assertEqual(runner1.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.error('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner('Runner1')
        runner2 = Runner('Runner2')
        for _i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, 100)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filemode='w', filename='module12/runner_tests.log', encoding='utf-8')
    unittest.main()
