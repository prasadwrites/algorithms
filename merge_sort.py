
def merge(arr, start , end):
    if (start >= end):
        return
    mid = (end+start)//2
    merge(arr, start, mid)
    merge(arr, mid+1, end)
    left = start
    right = mid+1
    aux = []

    while( left<=mid and right<=end):
        if (arr[left] <= arr[right]):
            aux.append(arr[left])
            left += 1
        elif(arr[right] <= arr[left]):
            aux.append(arr[right])
            right += 1
            
    while (left <= mid):
        aux.append(arr[left])
        left += 1    

    while (right <= end) :
        aux.append(arr[right])
        right += 1

    arr[start: end+1] = aux 
            
            

def merge_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    merge(arr, 0, len(arr)-1)
    return arr
