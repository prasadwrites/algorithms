
arr = [6,5,4,7,8,4,3,2,1,45,23,67,34]

def bubble_sort(arr):
    swapped, i, j = True, 0, 1
    length = len(arr) 
    while(swapped):
        i = 0
        swapped = False
        
        for i in range(0,length-j):
            if( arr[i] >= arr[i+1] ):
                temp = arr[i] 
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swapped = True
        j += 1


print(arr)
bubble_sort(arr)
print(arr)
