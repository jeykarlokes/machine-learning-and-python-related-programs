# selection_sort.py

def findsmallest(arr):
	smallelement = arr[0]
	smallelement_index = 0
	for i in range(1,len(arr)):
		if arr[i] < smallelement:
			smallelement = arr[i]
			smallelement_index = i
	return smallelement_index


# print(findsmallest([1,234,423,-2]))

def selectionsort(arr):
	newarr = []
	for i in range(len(arr)):
		smallest = findsmallest(arr)
		newarr.append(arr.pop(smallest))
	return newarr
print(selectionsort([1,234,423,-2]))
