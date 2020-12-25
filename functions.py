import random
import string
import time
import os
diction={}

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

def assign_code(file):
    file1 = open(file ,"r+")
    #if names is the list of student names
    roll=file1.readlines()
    file1.close()
    diction=roll
    file2 = open(file,"w+")
    for i in roll:
        a=i[:-1]
        file2.write(a+": "+code()+"\n")
    file2.close()
    return file

def student_dict():
    for i in diction:
        temp=i[:-1]
        i=temp.split(": ")
        diction[i[1]]=i[0]
    return diction