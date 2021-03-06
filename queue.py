from linkedlist import *

class queue(object):
    """docstring for Queue"""
    def __init__(self):
        self._store = dlinkedlist()
        self._size = 0

    def enqueue(self,value):
        self._store.backadd(value)
        self._size += 1

    def dequeue(self):
        if(self.isEmpty()):
            return None
        self._size -= 1
        return self._store.frontremove()

    def peek(self):
        return self._store.get(0)

    def size(self):
        return self._size 

    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False 

    def discard(self):
        if self.isEmpty():
            return None
        self._size -= 1
        return self._store.backremove()

    def extract(self):
        return self._store.extract()