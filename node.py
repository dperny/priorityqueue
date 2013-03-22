class Node:

    def __init__(self,head,tail):
        self._head = head
        self._tail = tail

    def head(self):
        return self._head

    def tail(self):
        return self._tail

    def setHead(self,value):
        self._head = value

    def setTail(self,node):
        self._tail = node