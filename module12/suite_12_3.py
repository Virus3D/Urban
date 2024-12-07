import unittest
from tests_12_3 import RunnerTest, TournamentTest

RunnerTournamentST = unittest.TestSuite()
RunnerTournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
RunnerTournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(RunnerTournamentST)
