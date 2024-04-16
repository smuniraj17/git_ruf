n=int(input('enter 1 if you your tax percentage of the bill//enter 2 if you dont know your tax percentage of the bill'))
if(n==1):
	t=eval(input('enter the tax%'))
	m=eval(input('enter the number of items'))
	a=eval(input('enter the %d names of items in LIST'%m))
	b=eval(input('enter the %d prices of items in LIST'%m))
	c=[]
	for i in b:
		c.append(round((i*(t/100)+i),2))
	for i in range(len(a)):
		print(f'product_name:{a[i]} \t price_before_tax:{b[i]} \t price_after_tax:{c[i]}')
	print('sub_total of the bill',sum(c))
else:
	d=eval(input('enter 1 if you your tax amount of the bill//enter 2 if you dont know your tax amount of the bill'))
	if(d==1):
		tax_amount=eval(input('enter the known tax amount'))
		total_amount_tax_excl=eval(input('enter the known total amount tax exclusive'))
		t=round(((tax_amount/total_amount_tax_excl)*100),2)
		m=eval(input('enter the number of items'))
		a=eval(input('enter the %d names of items in LIST'%m))
		b=eval(input('enter the %d prices of items in LIST'%m))
		c=[]
		for i in b:
			c.append(round(((i*(t/100))+i),2))
		for i in range(len(a)):
			print(f'product_name:{a[i]} \t price_before_tax:{b[i]} \t price_after_tax:{c[i]}')
		print('sub_total of the bill',sum(c))
	else:
		total_amount_tax_incl=eval(input('enter the known total amount tax inclusive'))
		total_amount_tax_excl=eval(input('enter the known total amount tax exclusive'))
		tax_amount=total_amount_tax_incl-total_amount_tax_excl
		t=round(((tax_amount/total_amount_tax_excl)*100),2)
		m=eval(input('enter the number of items'))
		a=eval(input('enter the %d names of items in LIST'%m))
		b=eval(input('enter the %d prices of items in LIST'%m))
		c=[]
		for i in b:
			c.append(round(((i*(t/100))+i),2))
		for i in range(len(a)):
			print(f'product_name:{a[i]} \t price_before_tax:{b[i]} \t price_after_tax:{c[i]}')
		print('sub_total of the bill',sum(c))
# d=eval(input('enter 1 if you wish to split any of the item with your friends'))







