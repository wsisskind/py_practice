def sqrsum1(i):
	sqrlist = []
	for j in range(i+1):
		if j < i:
			print(j, "squared is", j*j)
			sqrlist.append(j*j)
		elif j == i:
			print(j, "squared is", j*j)
			sqrlist.append(j*j)
			print('----------')
			print('The sum of these squares is:', sum(sqrlist))

def sqrsum2(i):
    sqrlist = []
    for j in range(i+1):
        sqrlist.append(j*j)
    print('The sum of all squares up to', i, 'is', sum(sqrlist), end='.\n')
        
