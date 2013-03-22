from linkedlist import *
from collections import deque

class queue(object):
    """docstring for Queue"""
    def __init__(self):
        self._store = deque()
        self._size = 0

    def enqueue(self,value):
        self._store.appendleft(value)
        self._size += 1

    def dequeue(self):
        if(self.isEmpty()):
            raise SizeError("queue is empty")
        self._size -= 1
        return self._store.pop()

    def peek(self):
        return self._store[0]

    def size(self):
        return self._size 

    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False 

    def discard(self):
        if self.isEmpty():
            raise SizeError("queue is empty")
        self._size -= 1
        return self._store.popleft()

    def extract(self):
        return list(self._store) 