size = int(input('Enter the Tree size: '))

for row_num in range(1,size + 1):
	print(' ' * (size - row_num)+'^' * (row_num * 2 - 1) )

for trunk in range(0,2):
	print(' '* (size - 2),"#" )