from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner1 = Runner('Runner1')
        for _i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    def test_run(self):
        runner1 = Runner('Runner1')
        for _i in range(10):
            runner1.run()
        self.assertEqual(runner1.distance, 100)
        
    def test_challenge(self):
        runner1 = Runner('Runner1')
        runner2 = Runner('Runner2')
        for _i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, 100)

if __name__ == '__main__':
    unittest.main()