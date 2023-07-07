#! /usr/env/path python
''' This solution is done using list and removes the immutable 
    string to avoid extra burden on time '''

def solutions():
    result=[]
    def helper(index,slate=None):
        if slate== None:
            slate=[]

        if len(slate) == bag_len:
            result.append(''.join(slate))
            return

        if(bag[index].isdigit()):
            slate.append(bag[index])
            helper(index+1, slate)
            slate.pop()
        else:
            slate.append(str(bag[index].upper()))
            helper(index+1,slate)
            slate.pop()
            slate.append(str(bag[index].lower()))
            helper(index+1, slate)
            slate.pop()

    slate1 = list()
    bag = list("a1b2c3")
    bag_len = len(bag)
    helper( 0, slate1)
    print(result)

solutions()