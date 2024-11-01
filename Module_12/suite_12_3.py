import unittest


from Module_12.Module_12_1.test import TestRunner
from Module_12.Module_12_2.test_run import TournamentTest

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestRunner))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
run = unittest.TextTestRunner(verbosity=2)
run.run(test_suite)