#!/usr/bin/env python
#test.py
#

from dfs import Graph, depthFirst

def main():


	#Initial node a
	a = Graph('a')

	#Children of a
	a.addchild(Graph('b'))
	a.addchild(Graph('d'))
	a.addchild(Graph('f'))

	#Children of b
	a.child[0].addchild(Graph('c'))
	a.child[0].addchild(a.child[2])

	#Children of c
	a.child[0].child[0].addchild(a.child[1])

	#Children of d
	a.child[1].addchild(a.child[0])

	#Children of f
	a.child[2].addchild(a.child[1])

	#e initialized seperately as it is not a child of any other node
	e = Graph('e')

	#Children of e - d and f
	e.addchild(a.child[1])
	e.addchild(a.child[2])

	#Initial dict of depth first numbers - unknown on all nodes
	nodes={'a':'inf','b':'inf','c':'inf','d':'inf','e':'inf','f':'inf'}
	nodes2={'a':'inf','b':'inf','c':'inf','d':'inf','e':'inf','f':'inf'}

	expM  = {'a':0,'b':1,'c':2,'d':3,'e':'inf','f':2}
	expN = {'a':'inf','b':2,'c':3,'d':1,'e':0,'f':3}


	print "Expected:"
	print "Depth First Search - Start Node a:"
	
	print expM

	print '\n',"Depth First Search - Start Node e:"

	print expN

	print '\n',"Resultant:"
	print "Depth First Search - Start Node a:"

	M = depthFirst(a,nodes)

	print M

	print '\n',"Depth First Search - Start Node e:"

	N = depthFirst(e,nodes2)

	print N

if __name__ == "__main__":
	main()
