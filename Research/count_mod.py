#!/bin/python3

import math
import os
import random
import re
import sys
s = "epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq"
n = 549382313570
# Complete the repeatedString function below.
# s = "udjlitpopjhipmwgvggazhuzvcmzhulowmveqyktlakdufzcefrxufssqdslyfuiahtzjjdeaxqeiarcjpponoclynbtraaawrps"
# n = 872514961806
s_count_a  = s.count("a")
# print("s count a = ",s.count("a"))
# def comoputemod(s,times,mod,length):
#     new_string = s * times 
#     # print("B",len(new_string))
#     new_string += s[:mod]
#     # print(mod)
#     # print("A",len(new_string))
#     return new_string
#     pass
def comoputeLength(n):
    return len(s)
def repeatedString(s, n):
    length  = comoputeLength(s)
    print(length)
    mod  = n % length
    times  = n//length
    max_limit = 10000000000000
    print("times",times)
    temp = times * s_count_a
    # print(temp)
    temp_len = s[:mod].count("a")
    # print(temp_len)
    final_result = temp_len + temp
    print(final_result)
    # if n>=1 and n <=max_limit: 
    #     if length == 1 and "a" in s:
    #         return n
    # pass     

result = repeatedString(s, n)
# print(int(result))
print("expected : 16481469408")