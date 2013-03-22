class Node:

    def __init__(self,next,value,prev):
        self._next = next
        self._value = value
        self._prev = prev

    def value(self):
        return self._value

    def next(self):
        return self._next

    def prev(self):
        return self._prev

    def setValue(self,value):
        self._value = value

    def setNext(self,node):
        self._next = node

    def setPrev(self,node):
        self._prev = node
