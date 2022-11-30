v=int(input())
t=int(input())
s=v*t
if s>109:
	s=abs(109-s)
	print(s)
else:
	print(s)