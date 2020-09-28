# TODO: complete the function "lowest_terms" below

def lowest_terms(x):
	"""
	Returns fractions in their lowest indivisible terms.
	cont (list) - container storing integer values
	factors (list) - stores factors
	result (list) - holds final result
	"""
	x = x.split('/')

	# count identifies the number of negatives in the fraction to determine its sign
	count = 0

	# Separating negative sign from values
	for i in x:
		if '-' in i:
			x[x.index(i)] = i[1:]
			count += 1

	# Converting strings to integers
	cont = [int(i) for i in x]

	# copy is a copy of the prepared input that wouldn't be altered
	copy = cont[:]

	"""
	Looping through the minimum value to obtain factors
	"""
	factors = [i+1 for i in range(min(cont)) if min(cont) % (i+1) == 0]

	# Reversing the list allows for dividing by larger common factors first before smaller ones
	factors.reverse()

	"""
	Loopint through and dividing by common factors
	"""
	for i in factors:
		if cont[0] % i == 0 and cont[1] % i == 0:
			cont[0] = cont[0] / i
			cont[1] = cont[1] / i

	# Converting integers back to strings
	cont = [str(i) for i in cont]

	# Removing decimal points caused by division process
	result = [i.split('.') for i in cont]

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