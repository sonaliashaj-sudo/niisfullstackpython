c = 4
for i in range(c,0,-1):
	for j in range(1,i+1):
		print(j,end="")
	for j in range(2*(c-i)):
		print(" ",end="")
	for j in range(i,0,-1):
		print(j,end="")
	print()	