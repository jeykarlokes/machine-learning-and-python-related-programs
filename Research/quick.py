from time import sleep
def quick(arr):
	if len(arr)	< 2:
		return arr
	else:
		pivot = arr[0]
		low = [i for i in arr[1:] if pivot > i]
		high = [i for i in arr[1:] if pivot <= i]
		return quick(low) + [pivot] + quick(high)
	pass
print(quick([1,12,1,21,131,134,1,12,121,1222]))

for i in [1,1,3,1,3,1341,3,12,1,113]:
	sleep(2)
	print("............")
	sleep(1)
	print(i)