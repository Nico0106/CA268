def get_counts(list):
	c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for n in list:
		c[len(n)] += 1
	return c
