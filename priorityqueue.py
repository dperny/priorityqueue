from queue import *
from collections import deque

class PriorityQueue:
    """A python3 class implementing a naive priority queue

    Uses an array of linked-list based queues. enqueues are O(1),
    dequeues are O(m) where m is the number of priority levels, and removing
    the lowest priority item is O(m)

    becomes bounded, because priority levels are set on initialization
    """

    def __init__(self,capacity,levels):
        self._store = [None] * levels
        self._capacity = capacity
        self._size = 0
        for i in range(levels):
            self._store[i] = queue()

    def enqueue(self,packet):
        """adds an item to the queue. if the queue is full, 
        removes the lowest priority item and return that item
        else returns None"""

        rval = None
        # if we're already at capacity
        if self._size == self._capacity:
            # discard the lowest priority item
            rval = self._discard()
        # enqueue into the queue based on the priority value of the packet
        self._store[packet[0]].enqueue(packet) 
        self._size += 1

        return rval

    def dequeue(self):
        """removes the highest priority item from the queue"""
        for i in range(len(self._store)-1,-1,-1):
            if not self._store[i].isEmpty():
                self._size -= 1
                return self._store[i].dequeue()
        return None

    def _discard(self):
        """private function that removes the lowest priority item"""
        for i in range(len(self._store)):
            if not self._store[i].isEmpty():
                rval = self._store[i].discard()
                break
        self._size -= 1
        return rval

    def extract(self):
        rlist = []
        for i in range(len(self._store)):
            rlist.append(self._store[i].extract())
        return rlist

    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False