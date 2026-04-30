scale = input('Enter C or F  to indicate Celsius or Fahrenheit: ')
degrees = float(input("Enter the number of degrees: "))

if scale == "C":
	if degrees >= 16 and degrees <= 38:
		print('Safe')
	else:
		print('Dangerous')
elif scale == "F":
	if degrees >= 60.8 and degrees <= 100.4:
		print("Safe")
	else:
		print("Dangerous")