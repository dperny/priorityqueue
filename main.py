import sys
from time import sleep
from priorityqueue import *
import random

class gatekeeper:
    def __init__(self,maxins):
        random.seed()
        self._maxInCount = maxins
        self._incounter = 0
        self._inStatus = True
        self._count = 0

    def tick(self):
        sleep(.1)
        self._count = (self._count + 1) % 128

    def output(self):
        if self._count % 4 == 0:
            return True

    def input(self):
        if self._incounter < 0:
            self._incounter -= 1
            return inStatus
        elif self._incounter == 0:
            self._incounter = random.randint(0,(maxins * 3)//2)
            self._instatus = False if random.randint(0,2) < 2 else True
            return self.input()

def main(argv):
    p_queue = PriorityQueue(argv[0],argv[1])
    keeper = gatekeeper(argv[0])



if __name__ == '__main__':
    main(sys.argv)