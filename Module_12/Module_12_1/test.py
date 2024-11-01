import unittest
from unittest import TestCase

from Module_12.Module_12_1.runner import runner, runner2


class TestRunner(TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Ок')
    def test_walk(self):
        runner.distance = 0
        for i in range(0, 10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner.distance = 0
        for i in range(0, 10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner.distance = 0
        runner2.distance = 0
        for i in range(0, 10):
            runner.walk()
            runner2.run()
        self.assertNotEqual(runner.distance, runner2.distance)
