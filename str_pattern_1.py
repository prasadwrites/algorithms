# !/usr/bin/env python

dictionary = { 'f': ['F', 4], 'b': ['B', 8, 9] }
strg = "fab"

#[FaB, Fa8, 4aB, 4a8]

stack = list()
results = list()
char = ""
def getResults(start_index):
    charu = strg[start_index]
    if charu in dictionary:
        for element in dictionary[charu]:
            stack.append(element)
            if start_index == len(strg)-1:
                results.append(''.join(map(str, stack)))
                stack.pop()
                continue
            getResults( start_index+1)
    else:
        stack.append( charu)
        getResults(start_index+1)
    if stack:
        stack.pop()
    else:
        return results

print getResults( 0)