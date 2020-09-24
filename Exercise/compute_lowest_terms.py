# TODO: complete the function "lowest_terms" below

def lowest_terms(x):
	x = x.split('/')
	l = []
	fac = []
	res = []
	count = 0
	for i in x:
		if '-' in i:
			x[x.index(i)] = i[1:]
			count += 1
	for j in x:
		l.append(int(j))
	copy = l[:]

	for i in range(min(l)):
		if min(l) % (i + 1) == 0:
			fac.append(i + 1)
	fac.reverse()

	for i in fac:
		if min(l) % i == 0 and max(l) % i == 0:
			l[l.index(min(l))] = min(l) / i
			l[l.index(max(l))] = max(l) / i

	for i in l:
		l[l.index(i)] = str(i)
	for i in l:
		res.append(i.split('.'))

	if copy[1] == 0:
		return 'Undefined'
	elif copy[0] == 0:
		return '0'
	else:
		if count == 0 or count == 2:
			return str(res[0][0]) + '/' + str(res[1][0])
		else:
			return '-'+str(res[0][0]) + '/' + str(res[1][0])


