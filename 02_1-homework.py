a=int(input())
b=int(input())
c=int(input())

if a==b and a==c:
	print('3')
elif a==b and b!=c:
	print('2')
elif b==c and b!=a:
	print('2')
else:
	print('0')