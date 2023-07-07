
arr = ['G','B','R','G','B','G','R']

ridx=0
bidx=len(arr)-1
i=0
while(i<bidx):
    if(arr[i] == 'R'):
        arr[i],arr[ridx] = arr[ridx],arr[i]
        ridx += 1 
        i = i+1
    elif (arr[i] == 'B'):
        arr[i],arr[bidx] = arr[bidx], arr[i]
        bidx -= 1
    else:
        i=i+1
print(arr)        
 