from node import Node

class LinkedList:

	def __init__(self,value = None):
		# if no value is passed in
		if(value == None):
			self._size = 0
			self._headNode = None
			self._tailNode = None
		else:
			self._headNode = Node(None,value,None)
			self._tailNode = self._headNode
			self._size = 1

	def get(self,index):
		self._verifyIndex(index)
		if(index == 0):
			return self._headNode.value()
		elif(index == self._size - 1):
			return self._tailNode.value()
		else:
			i = 0
			walk = self._headNode
			while(i < index):
				walk = walk.next()
				i += 1
			return walk.value()

	def set(self,index,value):
		self._verifyIndex(index)
		i = 0
		walk = self._headNode
		while(i < index):
			walk = walk.next()
			i += 1
		walk.setValue(value)

	def frontadd(self,value):
		if self._headNode is None:
			self._headNode = Node(None,value,None)
			self._tailNode = self._headNode
		else:
			self._headNode = Node(None,value,self._headNode)
			self._headNode
		self._size += 1

	def backadd(self,value):
		if self._tailNode is None:
			self.frontadd(value)
			return
		self._tailNode.setNext(Node(self._tailNode,value,None))
		self._tailNode = self._tailNode.next()

	def indexadd(self,index,value):
		if index == 0:
			self.frontadd(value)
			return
		if index > self._size:
			raise IndexError

		i = 0
		walk = self._headNode

		while i < (index - 1):
			walk = walk.next()
			i += 1
		walk.setNext(Node(walk,value,walk.next()))
		self._size += 1

	def indexremove(self,index):
		if(index == 0):
			rval = self.frontremove()
			return rval
		if(index == self._size - 1):
			rval = self.backremove()
			return rval
		self._verifyIndex(index)
		i = 0
		walk = self._headNode
		while(i < index-1):
			walk = walk.next()
			i += 1
		rval = walk.next().value()
		walk.setnext(walk.next().next())
		walk.next().setPrev(walk)
		self._size -= 1
		return rval

	def frontremove(self):
		if self._headNode is None:
			print("something broke (empty node)")
			return None
		assert self._headNode.value() is not None
		rval = self._headNode.value()
		assert rval is not None
		self._headNode = self._headNode.next()
		if self._headNode is not None:
			self._headNode.setPrev(None)
		self._size -= 1
		return rval

	def backremove(self):
		if self._tailNode is None:
			return None
		rval = self._tailNode.value()
		self._tailNode = self._tailNode.prev()
		if self._tailNode is not None:
			self._tailNode.setNext(None)
		self._size -= 1	
		if self._size == 0:
			self._headNode = None
			self._tailNode = None

		return rval

	def extract(self):
		if(self._headNode == None):
			return []
		rlist = []
		walk = self._headNode
		while(walk.next() is not None):
			rlist.append(walk.value())
			walk = walk.next()
		rlist.append(walk.value())

		return rlist

	def isEmpty(self):
		if self._size == 0:
			return True
		else:
			return False

	def size(self):
		return self._size

	def _verifyIndex(self,index):
		if(index > self._size-1):
			raise IndexError("index out of bounds")
		else: return