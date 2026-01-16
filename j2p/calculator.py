## calculator.py
result = 0

def add(num):
	global result
	result += num
	return result

print(add(3))  # Output: 3
print(add(4))  # Output: 8