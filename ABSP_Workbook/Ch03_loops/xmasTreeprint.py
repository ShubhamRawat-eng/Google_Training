import random
size = int(input('Enter size of tree: '))

for row_num in range(1,size+1):
	branch =(" " * (size - row_num))
	for branch_slot in range(0,2*row_num-1):
		if random.randint(1,4) == 1:
			branch = str(branch) + 'o'
		else:
			branch = str(branch) + "^"
	print(branch)

for trunk in range(0,2):
	print(' '*(size - 1) + '#')