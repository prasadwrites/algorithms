#usr/bin/env python


arr = [1,3,6,7,4,6,8,9,1,4,6,7]

for i in range(len(arr)):
	for j in range(i,len(arr)):
		if arr[j] < arr[i]:
			temp = arr[j]
			arr[j] = arr[i]
			arr[i] = temp

print(arr) 