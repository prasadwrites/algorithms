#! /usr/bin/env python

dictionary = { 1: 'a', 2 :'b', 3:'c' , 4:'d' , 5:'e' , 6:'f', 7:'g' , 8:'h' , 9:'i', 10:'j', 11:'k', 12:'l', 22:'w' }


string_list = list()
results = list()
finish = list()
num = 11223
string_num = str(num)
finish = list()


def reverseStr(result, previous):
    if result:
        current = result[-1]
    else:
        return
    if len(result) == 1:
        finish_string =''.join(map(chr,map(lambda x:x+96, map(int,list(reversed(finish))))))
        string = dictionary[int(current + previous)] + finish_string
        results.append(string)
        return
    if len(result) == len(string_num):
        previous = result[-1]
        reverseStr(result[:-1], previous)
        return


    str = ''.join(map(chr,map(lambda x:x+96 ,map(int,result))))


    if not finish:
        results.append( str[:-1] +   chr(96+int(current + previous)) )
    else:
        finish_string =''.join(map(chr,map(lambda x:x+96, map(int,list(reversed(finish))))))
        results.append( str[:-1] +   chr(96+int(current + previous)) +  finish_string)
    finish.append(previous)
    previous = current
    reverseStr(result[:-1], previous)


def getResults():
    result = ''
    print string_num
    for i in string_num:
        string_list.append(i)
        result += chr(96+ int(i))
    results.append(result)
    previous = ''
    reverseStr(string_num, previous)






getResults()
print results
