def check_brackets(line):
    import sys
	br = {"(":")"}
	left = Stack()
	right = Stack()
	for ch in line:
		if ch in br:
			left.push(ch)
		elif ch in check_br.values():
			if len(left) == len(right):
				return False
			left.push(ch)
	while not left.is_empty() and not right.is_empty():
		left.pop()
		right.pop()
	if left.is_empty() and right.is_empty():
		return True
	return False
