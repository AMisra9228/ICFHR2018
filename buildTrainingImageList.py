textfile=open('imagelist','w')
for i in range(1,31):
	textfile.write(f'data/signer_{str(i)}/genuine/signer{str(i)}sampNo1.png {str(i-1)}\n')
	textfile.write(f'data/signer_{str(i)}/genuine/signer{str(i)}sampNo2.png {str(i-1)}\n')
	textfile.write(f'data/signer_{str(i)}/genuine/signer{str(i)}sampNo3.png {str(i-1)}\n')
	textfile.write(f'data/signer_{str(i)}/genuine/signer{str(i)}sampNo4.png {str(i-1)}\n')
	textfile.write(f'data/signer_{str(i)}/genuine/signer{str(i)}sampNo5.png {str(i-1)}\n')

textfile.close()
