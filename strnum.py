alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def convert(num, min_length = 1):
	result = ''
	while num > 0:
		result = alphabet[num % 36] + result
		num = num // 36
	if len(result) < min_length:
		return '0' * (min_length - len(result)) + result
	return result

def digits(num, min_length = 1):
	count = 0
	while num > 0:
		num = num // 36
		count += 1
	return max(count, min_length)