#!/usr/bin/env python
#opdict.py - Open hash implementation of dictionary ADT. Uses mod B
#to hash values to buckets. 
#

def h(x,B):
	add = 0
	if isinstance(x,str):
		for i in range(0,len(x)):
			add = add + ord(x[i])
	else:
		add = x
	h = add % B
	return h

class Node:
	def __init__(self,car=None,link=None):
		self.car = None
		self.link = None

class opDict:
	def __init__(self,B=10):
		self.B = B
		self.data = [None] * B
		self.c = 1
	

	def INSERT(self,x):
		self.c = 1
		if not self.MEMBER(x):
			bucket = h(x,self.B)
			oldheader = self.data[bucket]
			self.data[bucket] = Node()
			self.data[bucket].car = x
			self.data[bucket].link = oldheader


	def DELETE(self,x):
		self.c = 1
		bucket = h(x,self.B)
		if self.data[bucket] != None:
			if self.data[bucket].car == x:
				self.data[bucket] = self.data[bucket].link
			else:
				current = self.data[bucket]
				while current.link != None:
					if current.link.car == x:
						current.link = current.link.link
					#	print "DELETE", x
						return
					else:
						current = current.link
						self.c = self.c + 1


	def MEMBER(self,x):
		current = self.data[h(x,self.B)]
		while current != None:
			if current.car == x:
				return True
			else:
				current = current.link
				self.c = self.c + 1
		return False


	def MAKENULL(self):
		for i in range(0, 0):
			self.data[i] = None
