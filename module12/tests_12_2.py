from runner_and_tournament import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_usain = Runner('Усэйн', 10)
        self.runner_andrey = Runner('Андрей', 9)
        self.runner_nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print();
        for results in cls.all_results:
            print(results)

    def test_race_usain_and_nik(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nik)
        results = tournament.start()
        self.all_results.append(results)
        
        last_runner_name = results[max(results.keys())]
        self.assertTrue(last_runner_name == self.runner_nik)

    def test_race_andrey_and_nik(self):
        tournament = Tournament(90, self.runner_andrey, self.runner_nik)
        results = tournament.start()
        self.all_results.append(results)
        
        last_runner_name = results[max(results.keys())]
        self.assertTrue(last_runner_name == self.runner_nik)

    def test_race_usain_and_andrey_and_nik(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nik)
        results = tournament.start()
        self.all_results.append(results)
        
        last_runner_name = results[max(results.keys())]
        self.assertTrue(last_runner_name == self.runner_nik)

    def test_race_fast_vs_slow(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nik)
        results = tournament.start()
        expected_order = ['Усэйн', 'Ник']
        finishers = [str(results[i]) for i in sorted(results.keys())]
        self.assertEqual(finishers, expected_order)

    def test_race_medium_vs_fast(self):
        self.tournament = Tournament(30, self.runner_andrey, self.runner_usain)
        results = self.tournament.start()
        expected_order = ['Усэйн', 'Андрей']
        finishers = [str(results[i]) for i in sorted(results.keys())]
        self.assertEqual(finishers, expected_order)

    def test_race_all(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nik)
        results = tournament.start()
        expected_order = ['Усэйн', 'Андрей', 'Ник']
        finishers = [str(results[i]) for i in sorted(results.keys())]
        self.assertEqual(finishers, expected_order)

if __name__ == '__main__':
    unittest.main()