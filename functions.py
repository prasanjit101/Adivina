import random
import string
import time
import os

def code():
    n=5
    res=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=n))
    return res


def timerFunction(seconds):
    timeLoop = 'y'
    while timeLoop:
        seconds -= 1
        print("Seconds Left: " + str(seconds))
        time.sleep(1)
        if seconds == 0:
            return True


def test_strings(*argv):
    for arg in argv:
        print(argv)
        if arg == '':
            return True
    return False