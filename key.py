d = {'Daniel': 'blue', 'Someone': 'blue', 'SomeoneTwo': 'red'}

def reverse_loopkup(dict_lookup, value):
	result = []
	for key in dict_lookup:
		if dict[key] == value:
			result.append(key)
	return result

print(reverse_loopkup(d,'blue')) #1, 2