#! /bin/env/path python

def printCombinations(slate,array):
	if (len(array)==0):
		print(slate)
		return
	printCombinations(slate,array[1:])
	printCombinations(slate+array[0], array[1:])


printCombinations("", "abcd")
