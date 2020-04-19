import time
import random
__low = 0
__high = 1048576

def gen(ghost = random.seed(), sig):
    while True:
        yield random.randint(__low, __high)
