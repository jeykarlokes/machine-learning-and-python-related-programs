no_elements = int(input())
elements = list(map(int,input().split()))
elements.sort()
mid = no_elements // 2
def odd(i):
    first_half = elements[:mid]
    second_half = elements[mid+1:]
    f_len = len(first_half)
    f = first_half[f_len] + first_half[f_len-1]
    s =second_half[f_len] + second_half[f_len-1]
    print(f/2)
    print(elements[mid])
    print(s/2)
#     pass
# def even():
#     first_half = elements[:mid]
#     second_half = elements[mid:]
#     f_len = len(first_half)
#     print(first_half[f_len])
#     print(elements[mid])
#     print(second_half[f_len])    
#     pass





if no_elements%2 != 0:
    odd(mid)
# even()
