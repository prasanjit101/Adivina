import random
import string
import time

def code():
    n=5
    res=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=n))
    return res

def time_lapse():
    start = time.time()
    while True:
        end = time.time()
        if (end - start)>3:
        #call a function to make the answer time time-out