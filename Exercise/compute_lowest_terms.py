# TODO: complete the function "lowest_terms" below

def lowest_terms(x):
	x = x.split('/')
	l = []
	fac = []
	res = []
	for i in x:
		l.append(int(i))
	print(l)

	for i in range(min(l)):
		if min(l) % (i + 1) == 0:
			fac.append(i + 1)
	fac.reverse()
	print(fac)

	for i in fac:
		if min(l) % i == 0 and max(l) % i == 0:
			print(i)
			l[l.index(min(l))] = min(l) / i
			l[l.index(max(l))] = max(l) / i
	print(l)
	for i in l:
		l[l.index(i)] = str(i)
	for i in l:
		res.append(i.split('.'))
	return str(res[0][0]) + '/' + str(res[1][0])
