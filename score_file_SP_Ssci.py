##### Score_file ########
DE_only = []
with open('new_DEs_only_SP_Ssci_FDR.csv') as DEs:
	for line in DEs:
		line = line.split()
		DE_only.append(line[0])
DE_only.pop(0)
#print(DE_only)
#print(len(DE_only))

anotated = []
with open('new_annotation_file_SP_Ssci.csv') as anot:
	for line in anot:
		line = line.split()
		anotated.append(line[0])

print(anotated)
print(len(anotated))

with open('score_file_SP_Ssci.txt', 'w') as output:
	for i in range(0, len(anotated)):
		if anotated[i] in DE_only:
			output.write(anotated[i]+'\t'+'0'+'\n')
		else:
			output.write(anotated[i]+'\t'+'1'+'\n')
