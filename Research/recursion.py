# def countdown(i):
# 	print(i)
# 	countdown(i-1)
# countdown(12)

# def sum(arr):
# 	total = 0
# 	for i in arr:
# 		total += i
# 	return total
# 	pass

# arr = [1,2,34,5,6,7,8,8]
# print(sum(arr))

# def recursion(arr):
# 	if arr == []:
# 		return 0
# 	else:
# 		# print(1 + recursion(arr[1:]))
# 		return 1 + recursion(arr[1:])
# 	pass

# arr = [1,2,34,5,6,7,8,8]

# print(recursion((arr)))


# 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 



def max(arr):
	if len(arr) == 2:
		return arr[0] if arr[0] > arr[1] else arr[1]
	else:
		print(arr[1:])
		max_i = max(arr[1:])
		print(max_i)
		return arr[0] if arr[0] > max_i else max_i
	pass
	
arr = [1,2,314,5,6,7,8]
(max(arr))