from pprint import pprint
from unittest import TestCase
from Module_12.Module_12_2.runner_and_tournament import Runner
from Module_12.Module_12_2.runner_and_tournament import Tournament


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usein = Runner('Усейн', speed=10)
        self.andrei = Runner('Андрей', speed=9)
        self.nik = Runner('Ник', speed=3)

    def test_start1(self):
        tournament = Tournament(90, self.usein, self.nik)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2] == 'Ник')

    def test_start2(self):
        tournament = Tournament(90, self.andrei, self.nik)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2] == 'Ник')

    def test_start3(self):
        tournament = Tournament(90, self.usein, self.andrei, self.nik)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[3] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            pprint(i)
