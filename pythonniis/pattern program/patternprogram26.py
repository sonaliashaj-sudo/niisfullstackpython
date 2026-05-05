c=4
for i in range(c):
	for j in range(c-i):
		print(chr(65+j),end="")
	for k in range(2*i):
		print(" ",end="")
	for j in range(c-i-1,-1,-1):
		print(chr(65+j),end="")
	print()	