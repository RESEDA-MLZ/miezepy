import os
import nose

argv = [
    '-v',
    '-s',
    '-w',
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'miezepy', 'tests'),
    '--processes', '0']

if __name__ == '__main__':
    nose.main(argv=argv)
