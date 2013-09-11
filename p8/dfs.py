#!/usr/bin/env python
#dfs.py - Depth First Search for graph objects. Returns a dictionary of
#depth first numbering for every node. If given a pre-existing dict of
#nodes, this program can mark which ones are not descendants of the starting
#node, as they will not be passed over or given new values.
#

class Graph():
	def __init__(self, car=None):
		self.car = car
		self.child = []
	def addchild(self,obj):
		self.child.append(obj)

def depthFirst(v, nums={}, M=[], c=0):
	if c == 0:
		M = []
	M.append(v.car)
	nums[v.car] = c
	c = c + 1
	for w in v.child:
		if w.car not in M:
			depthFirst(w,nums,M,c)
	return nums

