size_of_array = 10
m = 4
queries = [[2,6,8],[3,5,7],[1,8,1],[5,9,15]]

# !/bin/python3

# nm = input().split()
# size_of_array = int(nm[0])
# m = int(nm[1])
# queries = []
# for _ in range(m):
#     queries.append(list(map(int,input().rstrip().split())))

def arrayManipulation(n, queries):
    arr = [0]*n
    print(arr)
    queries = [[2,6,8],[3,5,7],[1,8,1],[5,9,15]]
    for i in queries:
        temp = i[0]-1
        print(temp)
        arr[temp] += i[2]

        print(arr[temp])
        print(i[1],"!=",len(arr))
        if i[1] != len(arr):
            arr[i[1]] -= i[2]
            print(arr[i[1]])
            # print(arr.index(i)
            print(arr)
    print(arr)
    
    maxval = 0
    itt = 0
    for q in arr:
        itt += q
        print(itt)
        if itt > maxval:
            maxval = itt
    print(maxval)

result = arrayManipulation(size_of_array, queries)
# print(result)
