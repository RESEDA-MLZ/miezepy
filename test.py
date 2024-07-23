import unittest
import os 

def suite():

    loader = unittest.TestLoader()
    tests = loader.discover(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'miezepy', 'tests'))

    return tests

if __name__ == '__main__':

    runner = unittest.TextTestRunner(verbosity=2, buffer=True)
    runner.run(suite())