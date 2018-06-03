textfile=open('Genuine_result')
for i in range(30):
	count=0
	for j in range(1,26):
		line=textfile.readline()
		f=lambda line: int(line.split('\t')[-1],10)
		class_res=f(line)
		#print(class_res)
		if(class_res!=i):	
			count=count+1
	print(f'Rate of misclassofication for class {i} -> {count/25*100}\n')
	
