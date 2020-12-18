import random
import string
import time

def code():
    n=5
    res=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=n))
    return res

def time_lapse():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time


start = time.time()
while True:
    end = time.time()
    if (end - start)>3:
        print("%.1f" %(end - start))
        start=end
