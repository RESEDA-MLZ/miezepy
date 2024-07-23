import unittest
from miezepy.core.module_environment import Environment


class Test_Environment(unittest.TestCase):

    def test_Environment_0(self):
        self.env = Environment(None, 'dummy')
        self.assertEqual(len(self.env.data), 1)
