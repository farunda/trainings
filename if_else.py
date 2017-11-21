while  True:
	age = int(input("Enter your age "))
	print(age)
	if 0 < age <= 7:
		print("You should go to kinder garden")
	elif 7 < age <= 16:
		print("go to school, kid")
	elif 16 < age <= 23:
		print("do you know what to do for diploma project?")
	elif 23 < age <= 65:
		print("go to work, mister")
	else:
		print("please, enter your age between 1 and 65")
		