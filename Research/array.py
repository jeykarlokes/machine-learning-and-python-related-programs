size_of_array= 10
m = 4
queries = [[2,6,8],[3,5,7],[1,8,1],[5,9,15]]
# 
# def create_array(size_of_array):
new_arr = [0 for i in range(size_of_array)]
	# return new_arr
	# pass


def calculate(i,j,k):
	index1 = i
	index2 = j
	value = k
	print(index1,index2,value)
	for i in range(index1-1,index2):
		new_arr[i] = new_arr[i]
		new_arr[i]+=value 
	return max(new_arr)

	pass
def index_val(array):
	new_arr = array
	# print(new_arr)
	temp = calculate(*array)
	return temp
	pass


def arrayManipulation(size_of_array, queries):
    # print(queries)
    # print(create_array(size_of_array))
    tempo = []
    for i in queries:
    	tempo.append(index_val(i))
    print(max(tempo))
    pass

    
result = arrayManipulation(size_of_array, queries)

