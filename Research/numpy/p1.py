no_of_test_case = int(input())
def spit_N(N):
	value = N //2
	diff  = N-value
	value_str = str(value)
	diff_str = str(diff)
	if "4" in value_str or "4" in diff_str:
		v = value_str.replace("4","2")
		diff_str = diff_str.replace("4","6")
		return v,diff_str
	return value,diff

if no_of_test_case >=1 and no_of_test_case <= 100:
    for i in range(no_of_test_case):
    	N=int(input())
    	max_limit  = 1000000000
    	if "4" in str(N) and N > 1:
    		if N < max_limit:
	    		a,b = spit_N(N)
    			print("Case #"+str(i+1)+":",a,b)
    			