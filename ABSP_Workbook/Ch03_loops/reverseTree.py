size = int(input('Enter the Tree size: '))

for trunk in range(0,2):
	print(' '* (size - 2),"#" )

for row_num in range(size,0,-1):
	print(' ' * (size - row_num)+'^' * (row_num * 2 - 1) )
