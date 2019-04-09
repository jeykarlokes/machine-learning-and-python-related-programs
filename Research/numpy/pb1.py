no_of_test_case = int(input())
assert no_of_test_case >=1 and no_of_test_case <= 100

def spit_N(N):
	value = N //2
	return value,N-value
	pass
for i in range(no_of_test_case):
	N = int(input())
	if not N < 1:
		a,b = (spit_N(N))
		print(f"Case #{i}:",a,b)
