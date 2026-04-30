unit = input("Enter TB or GB for the advertised unit: ")

#Calculate the amount that the advertised capacity lies:
if unit == "TB" or unit == "tb":
	discrepancy = 1000000000000 / 1099511627776
elif unit == "GB" or unit == "gb":
	discrepancy = 1000000000 / 1073741824
else:
	print("Please choose from TB or GB.Defaulting to GB.")
	discrepancy = 1000000000 / 1073741824
 
advertised_capacity = float(input("Enter the advertised capacity: "))

# Calculate the real capacity, round it to the nearest hunderdths,
# and convert  it to a string so it cna be concatenated:
real_capacity = str(round(advertised_capacity * discrepancy, 2))

print(f"The actual capacity is {real_capacity} {unit}")