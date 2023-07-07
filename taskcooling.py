# !/usr/bin/env python

#string = 'aabac'
string = "aabac"
coolingTime = 2
dictionary = {}
pList = list()

def getTimeTaken(pString, pCoolTime):

    time_count = 0
    tString = ''
    for element in pString:
        if pList :
            if dictionary [pList[0]] <= 0 :
                time_count += 1
                tString = tString + element
                for key in dictionary:
                    dictionary[key] = dictionary[key] - 1
                dictionary[pList[0]] = pCoolTime
                pList.remove(pList[0])



        if element not in dictionary :
            time_count += 1
            tString = tString + element
            for key in dictionary:
                dictionary[key] = dictionary[key] - 1
            dictionary[element] = pCoolTime


        else:
            if dictionary[element] <= 0:
                time_count += 1
                tString = tString + element
                for key in dictionary:
                    dictionary[key] = dictionary[key] - 1
                dictionary[element] = pCoolTime
            else:
                pList.append(element)


    while(pList):
        if dictionary[pList[0]] <= 0:
            time_count += 1
            tString = tString + pList[0]
            for key in dictionary:
                dictionary[key] = dictionary[key] - 1
            dictionary[pList[0]] = pCoolTime
            pList.remove(pList[0])

        else:
                tString = tString + '-'
                time_count += 1
                for key in dictionary:
                    dictionary[key] = dictionary[key] - 1



    return time_count



print "Total time taken %d" %getTimeTaken(string, coolingTime)