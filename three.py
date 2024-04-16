def fact(num):
	res=1
	while(num>1):
		res=res*num
		num=num-1
	return res
print(fact(int(input('enter the number'))))
