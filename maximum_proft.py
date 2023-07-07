def maxProfit(arr):
	max_profit = 0
	diff = 0
	mlen = len(arr)
	for i in range(mlen):
	    for j in range( i+1 ,mlen):
	        if arr[i] < arr[j]:
	            diff = arr[j] - arr[i]
	        if max_profit < diff:
	            max_profit = diff
	return max_profit

arr = [0, 6, 10, 3, 2, 80, -1, 10, 1]
print(maxProfit(arr))