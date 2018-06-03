import os
textfile=open('Genuine_testlist','w')

for j in range(1,11):
	for i in range(6,31):
		textfile.write(f'data/signer_{str(j)}/genuine/signer{str(j)}sampNo{str(i)}.png {str(j-1)}\n')
	
textfile.close()
