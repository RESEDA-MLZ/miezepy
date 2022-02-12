from miezepy.mieze import Mieze
import sys
import os
import traceback
from time import sleep
try:
    if __name__ == '__main__':
        print()
        os.system(
            'python -m miezepy.mieze '
            + (' '.join(sys.argv[1:]) if len(sys.argv[1:]) > 1 else ''))

except:
    print(sys.exc_info()[0])
    print(traceback.format_exc())
    print('Press Enter to Continue...')
    
    input()
