from node import Node

class dlinkedlist:
	def __init__(self):
		self.size = 0
		self._headNode = None
		self._tailNode = None
	
	def get(self,index):
		if index < size:
			walk = self._headNode
			for i in range(index):
				walk = walk.next
			return walk.value
		else: raise IndexError("out of bounds")
	
	def set(self,index,value):
		if index < size:
			walk = self._headNode
			for i in range(index):
				walk = walk.next
			walk.value = value
		else: raise IndexError("out of bounds")
	
	def frontadd(self,value):
		self._headNode = Node(None,value,self._headNode)
	
		if self._headNode.next is not None:
			self._headNode.next.prev = self._headNode
	
		if self._tailNode is None:
			self._tailNode = self._headNode
	
		self.size += 1
	
	def backadd(self,value):
		self._tailNode = Node(self._tailNode,value,None)
	
		if self._tailNode.prev is not None:
			self._tailNode.prev.next = self._tailNode
	
		if self._headNode is None:
			self._headNode = self._tailNode
	
		self.size += 1
	
	def indexadd(self,index,value):
		if index < size:
			walk = self._headNode
			for i in range(index):
				walk = walk.next
	
			if walk is not None:
				walk.prev = Node(walk.prev,value,walk)
				if walk.prev.prev is not None:
					walk.prev = walk.prev.prev.next
			self.size += 1
	
		else: raise IndexError("out of bounds")
	
	def frontremove(self):
		node = self._headNode
		if node is None:
			return None
	
		self._headNode = self._headNode.next
		if self._headNode is not None:
			self._headNode.prev = None
	
		self.size -= 1
		return node.value
	
	def backremove(self):
		node = self._tailNode
		if node is None:
			return None
	
		self._tailNode = self._tailNode.prev
		if self._tailNode is not None:
			self._tailNode.next = None
	
		self.size -= 1
		return node.value
	
	def indexremove(self,index):
		if index < size:
			walk = self._headNode
			for i in range(index):
				walk = walk.next
			walk.prev.next = walk.next.prev
			size -= 1
			return walk.value
		else: raise IndexError("out of bounds")
	
	def isEmpty(self):
		return True if size == 0 else False