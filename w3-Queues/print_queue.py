def print_queue(list, f, b):
	if b < f:
		for i in list[f:]:
			print(i)
		for i in list[:b]:
			print(i)
	else:
		for i in list[f:b]:
			print(i)
