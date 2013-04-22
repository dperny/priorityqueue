import sys
from time import sleep
from priorityqueue import *
import random
import datetime

ENQUEUE = 0
DEQUEUE = 1

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
            self._instatus = (False if random.randint(0,5) < 5 else True)
            if empty:
                self._instatus = True
            return self.input(empty)

class timetable:
    def __init__(self,sizes,filename,operations):
        self.filename = filename
        # the store is the number of sizes
        self._store = [None] * (sizes + 1)
        self.operations = operations
        self.sizes = sizes
        # every index in store has one deque for each operation
        for index in range(len(self._store)):
            self._store[index] = [deque()] * operations


    def addtime(self,size,operation,time):
        self._store[size][operation].append(time)

    def closeout(self):
        averages = [None] * (self.sizes + 1)
        for time in range(len(self._store)):
            averages[time] = []
            for deck in self._store[time]:
                averages[time].append(sum(deck)/float(len(deck)))

        outstring = "" 
        for i in range(len(averages)):
            outstring = outstring + str(i) + ' '
            for operation in averages[i]:
                outstring = outstring + str(operation) + ' '
            outstring = outstring + '\n'

        with open(self.filename,'w') as fp:
            fp.write(outstring)


def main(argv):
    if len(argv) < 3:
        print("usage: python3 main.py queuesize priorities ticktime")
        return -1
    queuesize = int(argv[1])
    priorities = int(argv[2])
    ticktime = float(argv[3])

    p_queue = PriorityQueue(queuesize,priorities)
    keeper = gatekeeper(queuesize,ticktime)
    times = timetable(queuesize,"naive.txt",2)
    random.seed()

    def generate_datum(value):
        return random.randint(0,priorities-1),value

    i = 0

    while True:
        try:
            keeper.tick()   

            if keeper.input(p_queue.isEmpty()):
                datum = generate_datum(i)
                i += 1
                print("packet {0} was buffered".format(datum))
                start = datetime.datetime.now()
                discard = p_queue.enqueue(datum)
                end = datetime.datetime.now()
                times.addtime(p_queue.size,ENQUEUE,(end - start).microseconds)
                if discard is not None:
                    print("overflow: discarded value{0}".format(discard))
            if keeper.output():
                if p_queue.isEmpty():
                    print("the queue is empty")
                    i = 0
                else:
                    start = datetime.datetime.now()
                    newvar = p_queue.dequeue()
                    end = datetime.datetime.now()
                    times.addtime(p_queue.size,ENQUEUE,(end - start).microseconds)
                    print("packet {0} was dequeued".format(newvar))
        except KeyboardInterrupt:
            break

    print("exited peacefully")
    times.closeout()


if __name__ == '__main__':
    main(sys.argv)