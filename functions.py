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

def assign_code():
    file = open(r"data.txt","a+")
    #if names is the list of student names
    for i in names:
        file.write(i+"-"+str(code()))

def get_students_code():
    file=open(r"data.txt","")