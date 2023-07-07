#!/usr/bin/env python


def mergeLists(L1 , L2):
    len1 = len(L1)
    len2 = len(L2)
    print len1
    print len2
    index1 = 0
    index2 = 0
    pickx = 0
    picky = 0
    mergeList = []
    while (L1[index1][1] > L2[index2][0]):
        if (L1[index1][0] < L2[index2][0]):
            pickx = L2[index2][0]
        else:
            pickx = L1[index1][0]
        if (L1[index1][1] < L2[index2][1]):
            picky = L1[index1][1]
        else:
            picky = L2[index2][1]
        print "%d , %d" %(pickx,picky)
        mergeList.append([pickx,picky])
        index2 = index2+1
        if (index2 == len2):
            print "break"
            break

        if (L2[index2][0] < L1[index1][1]):
            continue
        else:
            index1 = index1 + 1
        if (index1 == len1-1):
            exit

    return mergeList


L1 = [[0,4], [7,12]]
L2 = [[1,3], [5,8], [9,11]]
print mergeLists(L1, L2)
