#!/usr/bin/env python
#test.py
#

import floyd
import sys

def main():
	INFIN = 1000

	D=[[0,4,1,5,8,10],[INFIN,0,INFIN,INFIN,INFIN,INFIN],[INFIN,2,0,INFIN,INFIN,INFIN],[INFIN,INFIN,INFIN,0,2,INFIN],[INFIN,INFIN,INFIN,INFIN,0,1],[INFIN,INFIN,INFIN,INFIN,INFIN,0]]

	expOp =[[0,3,1,5,7,8],[INFIN,0,INFIN,INFIN,INFIN,INFIN],[INFIN,2,0,INFIN,INFIN,INFIN],[INFIN,INFIN,INFIN,0,2,3],[INFIN,INFIN,INFIN,INFIN,0,1],[INFIN,INFIN,INFIN,INFIN,INFIN,0]]

	expP =[[0,3,0,0,4,5],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,5],[0,0,0,0,0,0],[0,0,0,0,0,0]]

	print "Original chart, INFINITY = ", INFIN, ": "
	print ' ','{:^8}{:^8}{:^8}{:^8}{:^8}{:^8}'.format('1','2','3','4','5','6')

	c = 1
	for n in D:
		sys.stdout.write(str(c))
		for i in n:
			sys.stdout.write('{:^8}'.format(str(i)))
		sys.stdout.write('\n')
		c = c + 1

	print '\n',"Expected:"
	print "Optimal chart: "
	print ' ','{:^8}{:^8}{:^8}{:^8}{:^8}{:^8}'.format('1','2','3','4','5','6')

	c = 1
	for n in expOp:
		sys.stdout.write(str(c))
		for i in n:
			sys.stdout.write('{:^8}'.format(str(i)))
		sys.stdout.write('\n')
		c = c + 1

	print '\n',"P chart: "
	print ' ','{:^8}{:^8}{:^8}{:^8}{:^8}{:^8}'.format('1','2','3','4','5','6')

	c = 1
	for n in expP:
		sys.stdout.write(str(c))
		for i in n:
			sys.stdout.write('{:^8}'.format(str(i)))
		sys.stdout.write('\n')
		c = c + 1


	print '\n',"Resultant:"
	
	B = floyd.floyd(D)
	print "Optimal chart: "
	print ' ','{:^8}{:^8}{:^8}{:^8}{:^8}{:^8}'.format('1','2','3','4','5','6')
	
	c = 1
	for n in D:
		sys.stdout.write(str(c))
		for i in n:
			sys.stdout.write('{:^8}'.format(str(i)))
		sys.stdout.write('\n')
		c = c + 1

	print '\n',"P chart: "
	print ' ','{:^8}{:^8}{:^8}{:^8}{:^8}{:^8}'.format('1','2','3','4','5','6')

	c = 1
	for n in B:
		sys.stdout.write(str(c))
		for i in n:
			sys.stdout.write('{:^8}'.format(str(i)))
		sys.stdout.write('\n')
		c = c + 1

#	print '\n',"Optimal path between node 1 and node 6 (P array test):"
#	floyd.path(B,0,5)
#	print ""


if __name__ == "__main__":
	main()
