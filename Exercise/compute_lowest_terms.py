# TODO: complete the function "lowest_terms" below

def lowest_terms(x):
	"""
	Returns fractions in their lowest indivisible terms.
	cont (list) - container storing integer values
	factors (list) - stores factors
	result (list) - holds final result
	"""
	x = x.split('/')
	cont = []
	factors = []
	result = []

	# count identifies the number of negatives in the fraction to determine its sign
	count = 0

	# Separating negative sign from values
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
	Looping through the minimum value to obtain factors
	"""
	for i in range(min(cont)):
		if min(cont) % (i + 1) == 0:
			factors.append(i + 1)

	# Reversing the list allows for dividing by larger common factors first before smaller ones
	factors.reverse()

	"""
	Division by common factors
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
	Using if conditions to handle division of and by zero and also to decide
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
