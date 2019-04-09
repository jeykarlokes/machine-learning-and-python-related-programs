s = input()
n = int(input())
s_count_a = s.count("a")
def repeatedString(s, n):
    length  = len(s)
    mod  = n % length
    times  = n//length
    temp = times * s_count_a
    temp_len = s[:mod].count("a")
    final_result = temp_len + temp
    print(final_result)
result = repeatedString(s, n)