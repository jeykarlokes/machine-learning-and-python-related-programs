a = [1,2,3,5,7,9,10,11]
def binary(a,item):
	low  = 0
	high = len(a)-1
	while low <= high:
		mid = (low+high)//2
		guess = a[mid]
		print(guess)
		if guess == item:
			return mid
		elif guess > item:
			high = mid-1
		else:
			low = mid + 1
	return None
	pass
print(binary(a,11))
