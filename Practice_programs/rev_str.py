def reverse_str(str):
	new_str = ""
	for i in str:
		new_str = i + new_str
	return new_str

str = "hello world"
print(reverse_str(str))

