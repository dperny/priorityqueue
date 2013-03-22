import sys
from time import sleep
from priorityqueue import *
import random

class gatekeeper:
    def __init__(self,maxins,ticktime):
        random.seed()
        self._ticktime = ticktime
        self._maxInCount = maxins
        self._incounter = 0
        self._inStatus = True
        self._count = -1 

    def tick(self):
        sleep(self._ticktime)
        self._count = (self._count + 1) % 128

    def output(self):
        if self._count % 4 == 0:
            return True

    def input(self,empty):
        if self._incounter > 0:
            self._incounter -= 1
            return self._instatus
        elif self._incounter == 0:
            self._incounter = random.randint(0,(self._maxInCount * 3)//2)
            self._instatus = (False if random.randint(0,2) < 2 else True)
            if empty:
                self._instatus = True
            return self.input(empty)

def main(argv):
    if len(argv) < 3:
        print("usage: python3 main.py queuesize priorities ticktime")
        return -1
    queuesize = int(argv[1])
    priorities = int(argv[2])
    ticktime = float(argv[3])

    p_queue = PriorityQueue(queuesize,priorities)
    keeper = gatekeeper(queuesize,ticktime)
    random.seed()

    def generate_datum(value):
        return random.randint(0,priorities-1),value

    i = 0

    while True:
        keeper.tick()

        if keeper.input(p_queue.isEmpty()):
            datum = generate_datum(i)
            i += 1
            print("packet {0} was buffered".format(datum))
            discard = p_queue.enqueue(datum)
            if discard is not None:
                print("overflow: discarded value{0}".format(discard))
        if keeper.output():
            if p_queue.isEmpty():
                print("the queue is empty")
                i = 0
            else:
                print("packet {0} was dequeued".format(p_queue.dequeue()))


if __name__ == '__main__':
    main(sys.argv)