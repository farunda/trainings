def string_comparsion(string_1, string_2):
	if string_1 == string_2:
		return 1
	elif len(string_1) > len(string_2):
		return 2
	elif string_2 == "learn":
		return 3
	else:
		return 42

string_1 = input("enter the first string: ")
string_2 = input("enter the second string: ")

print(string_comparsion(string_1, string_2))