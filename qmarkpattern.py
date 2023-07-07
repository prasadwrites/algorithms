#!/usr/bin/env python
str = "a??b?"
string = list(str)

dictionary = {'?':['0','1']}

results = list()
result_str = ''
start = -1

def getResults(word, start):
    for element in word[start:]:
        start += 1
        if start == len(word):
            if element == '?':
                word[start-1] =dictionary[element][0]
                results.append(''.join(word))
                word[start-1] =dictionary[element][1]
                results.append(''.join(word))
                return
            results.append(''.join(word))
            return
        if element == '?':
            word[start-1] =dictionary[element][0]
            getResults(word, start)
            word[start-1] = dictionary[element][1]
            getResults(word, start)




start = 0
getResults(string, start)
print results
