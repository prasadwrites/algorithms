
arr=[5,4,8, 10,-4]
k=6
def check_if_sum_possible(arr, k):

    slate = []
    index = 0
    arrlen = 0
    if arr:
        arrlen = len(arr)
    def printSubset(index, slate):
        #base case
        if(index==arrlen):
            sum = 0
            if slate:
                for i in range(len(slate)):
                    sum = sum + slate[i]
                if sum == k:
                    print(slate, end=" ")
                    return True
                else:
                    return False
                return
            else:
                return False

        if(printSubset(index+1,slate)):
            return True
        slate.append(arr[index])
        if(printSubset(index+1,slate)):
            return True
        slate.pop()
    if(printSubset(index,slate)):
        return True
    return False

print(check_if_sum_possible(arr, k))