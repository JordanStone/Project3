NAMES: Jordan Stone, Greg Fisher

CONTENTS: 
Code is submitted for problems 1,2,5,6,7,8. All program code is
written in python and is stored in the .py format.

	Folder hw3jls564gdf26:
		README.txt - text document detailing files submitted in this project and
		completeness of every section.

		REPORT.txt - text document detailing probe behavior observed in p1 and p2.


	Folder p1:
		opdict.py - contains code for the opDict class, an open hash
		implementation of the dictionary ADT, using pointers.

		test.py - test code that measures average probes on INSERT and DELETE
		methods of opDict, using several values for alpha. Details of results in
		REPORT.txt.

		Makefile - allows running of the code via "make" or "make test", and
		cleaning of classfiles through "make clean".


	Folder p2:
		closedHash.py - contains code for the closedHash class, a closed hash
		implementation of dictionary ADT.

		test.py - test code that measures average probes on INSERT and DELETE
		methods of closedHash, using several values for alpha. Details of results
		in REPORT.txt.

		Makefile - allows running of the code via "make" or "make test", and
		cleaning of classfiles through "make clean".


	Folder p5:
		dijkstra5.py - contains code for Dijkstra's shortest path algorithm on
		an adjacency matrix, representing a graph.

		test.py - test code that checks capability of dijkstra5's dijkstra
		function on the graph from problem 6 on review 2.

		Makefile - allows  running of the code via "make" or "make test", and
		cleaning of classfiles through "make clean".


	Folder p6:
		dijkstra6.py - contains code for Dijkstra's shortest path algorithm using
		a priority queue, on a linked adjacency list representing a graph. 

		test.py - test code that checks capability of dijkstra6's dijkstra
		function on the graph from problem 6 on review 2

		Makefile - allows  running of the code via "make" or "make test", and
		cleaning of classfiles through "make clean".


	Folder p7:
		floyd.py - contains code for Floyd's shortest path algorithm with
		recovery of paths. Includes a path function to test the returned P chart.

		test.py - test code that checks capability of floyd's floyd function on
		problem 6 of review 2. Displays the original, optimal, and P chart. Also
		includes a test of the path function, unenabled(commented) by default as
		it is not part of the required output.

		Makefile - allows  running of the code via "make" or "make test", and
		cleaning of classfiles through "make clean".

	Folder p8:
		dfs.py - contains code for depth first search for graphs - implemented
		here as a node class that consists of a value and an array of pointers to
		child nodes. depthFirst function returns a dictionary of depth first
		numbering for every node in the graph, based off the starting node.

		test.py - test code that checks capability of the depthFirst function by
		running it on fig 6.38 on page 226 of Data Structures and Algorithms. The
		function is started at both node a and node e.

		Makefile - allows  running of the code via "make" or "make test", and
		cleaning of classfiles through "make clean".

 
COMPLETE:
	Problems p1, p2, p5, p6, p7, and p8 are complete.


COMPILATION & EXECUTION:
	As described above, every problem folder contains a Makefile that will run
	the test code by either "make" or "make test". This will run the test.py in
	all problem folders.


TEST CASES:
	Test for p1 compares average probe count of INSERT and DELETE for several
	opDict objects to their expected bound at O(1+a).

	Test for p2 compares average probe count of INSERT and DELETE for several
	closedHash objects to their aproximate value of (1+1/(1-a)^2)/2 and
	(1+1/(1-a))/2, respectively.

	Test of p5 compares the result of the dijkstra function to arrays of
	expected values. Expected P list is for values expected of an array/graph
	starting at 0	instead of 1.

	Test of p6 compares the result of the dijkstra function to arrays of
	expected values. Expected P list is for values expected of an array/graph
	starting at 0 instead of 1.

	Test of p7 compares result of the floyd function to 2D arrays of expected
	values. Expected P list for values expected of a 2D array starting at 1, as
	experimental P values are altered to display as such.

	Test of p8 compares result of depthFirst function to dictionaries of
	expected nodes to values.

PROGRAM OUTPUT: 
	None of the class or function Python files (i.e., any Python file
	that is not a test.py), should output anything unless there is an error.

	Test.py for p1 will output the average probes for INSERT and DELETE for
	several values of a and the expected value of O(1 + a)

	Test.py for p2 will output the average probes for INSERT and DELETE for
	several values of a and the expected values of (1+1/(1-a)^2)/2 and
	(1=1/(1-a))/2.

	Test.py for p5 will output the expected and resultant D and P arrays from
	running a given 2D array C through dijkstra.

	Test.py for p6 will print the expected and resultant D and P values from
	running a given partially ordered tree through disktra. 

	Test.py for p7 wil output the original 2D array representing a graph,
	followed by the  expected and resultant optimal graph distance charts and
	the P charts, used to recover the optimal paths.

	Test.py for p8 outputs the expected and resultant dictionaries for running a
	given graph through the DFS, starting with Node a and Node e.
