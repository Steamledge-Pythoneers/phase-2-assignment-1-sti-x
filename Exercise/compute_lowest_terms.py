# TODO: complete the function "lowest_terms" below

def lowest_terms(x):
	"""
	Reducing fractions basically requires finding factors and dividing by them.
	Containers (lists) are created e.g cont, factors and results to hold these
	generated values.
	"""
	x = x.split('/')
	cont = []
	factors = []
	result = []

	# count identifies the number of negatives in the fraction to determine its sign
	count = 0

	# Separating negatives from values
	for i in x:
		if '-' in i:
			x[x.index(i)] = i[1:]
			count += 1

	# Converting strings to integers
	for j in x:
		cont.append(int(j))

	# copy is a copy of the prepared input that wouldn't be altered
	copy = cont[:]

	"""
	Only the factors of the minimum value of either numerator or denominator are required
	because any number greater than the minimum value wouldn't be a common factor for both
	numerator and denominator and thus wouldn't be able to divide both. Thus we loop
	through the minimum value 
	"""
	for i in range(min(cont)):
		if min(cont) % (i + 1) == 0:
			factors.append(i + 1)

	# Reversing the list allows for dividing by larger common factors first before smaller ones
	factors.reverse()

	"""
	loop through the factors of the minimum values and reduce the fraction by common 
	factors. This is done in-place so that the numerator and denominators are divided
	till it is no longer possible
	"""
	for i in factors:
		if min(cont) % i == 0 and max(cont) % i == 0:
			cont[cont.index(min(cont))] = min(cont) / i
			cont[cont.index(max(cont))] = max(cont) / i

	# Converting integers back to strings
	for i in cont:
		cont[cont.index(i)] = str(i)

	# Removing decimal points caused by division process
	for i in cont:
		result.append(i.split('.'))

	"""
	if conditions are used to handle division of and by zero and also to decide
	return values
	"""
	if copy[1] == 0:
		return 'Undefined'
	elif copy[0] == 0:
		return '0'
	else:
		if count == 0 or count == 2:
			return str(result[0][0]) + '/' + str(result[1][0])
		else:
			return '-'+str(result[0][0]) + '/' + str(result[1][0])
