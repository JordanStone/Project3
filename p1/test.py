#!/usr/bin/env python
#test.py
#

from __future__ import division
from random import randint
import opdict

def main():
	RANGE = [10,100,1000]
	sums = [0,0,0]

	d = opdict.opDict(10)
	e = opdict.opDict(10)
	f = opdict.opDict(10)

	num = []
	num2 = []
	num3 = []

	for i in range(0,RANGE[0]):
		num.append(randint(-1000,1000))
		d.INSERT(num[i])
		sums[0] = sums[0] + d.c

	for i in range(0,RANGE[1]):
		num2.append(randint(-1000,1000))
		e.INSERT(num2[i])
		sums[1] = sums[1] + e.c

	for i in range(0,RANGE[2]):
		num3.append(randint(-1000,1000))
		f.INSERT(num3[i])
		sums[2] = sums[2] + f.c

	print "INSERT:"
	print '{0:^20}{1:^20}{2:^20}'.format('a','Avg Probes','O(1 + a)')

	for n in range(0,3):
		avg = sums[n]/RANGE[n]
		a = RANGE[n]/10
		print '{0:20}{1:20.3f}{2:20.3f}'.format(a,avg,(a+1))

	sums = [0,0,0]

	for i in range(0,RANGE[0]):
		d.DELETE(num[i])
		sums[0] = sums[0] + d.c

	for i in range(0,RANGE[1]):
		e.DELETE(num2[i])
		sums[1] = sums[1] + e.c
	
	for i in range(0,RANGE[2]):
		f.DELETE(num3[i])
		sums[2] = sums[2] + f.c

	print "DELETE:"
	print '{0:^20}{1:^20}{2:^20}'.format('a','Avg Probes','O(1 + a)')

	for n in range(0,3):
		avg = sums[n]/RANGE[n]
		a = RANGE[n]/10
		print '{0:20}{1:20.3f}{2:20.3f}'.format(a,avg,(a+1))

if __name__ == "__main__":
	main()
