#!/usr/bin/env python
#floyd.py - Takes in a 2D array of distances between (numerically) named
#nodes and passes the optimal distances back to the original array. Returns
#an array P which can be used to recover the optimal paths.
#
#path function is included for testing - given a P array, a start node and
#end node, the function will print all other nodes (excluding the original
#two nodes) the path will pass through for the optimal path.
#

import sys

def floyd(C):
	n = len(C)
	A = C
	P = []
	for i in range(0,n):
		P.append([0])
		for j in range(1,n):
			P[i].append(0)
	for i in range(0,n):
		A[i][i] = 0
	for k in range(0,n):
		for i in range(0,n):
			for j in range(0,n):
				if A[i][k] + A[k][j] < A[i][j]:
					A[i][j] = A[i][k] + A[k][j]
					P[i][j] = k+1
	return P

def path(P,i,j):
	k = P[i][j]
	if k == 0:
		return
	path(P,i,k-1)
	sys.stdout.write(str(k)+' ')
	path(P,k-1,j)
