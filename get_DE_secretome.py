whole_secretome = []
with open('secretome_IDs.txt') as whole:
	for line in whole:
		line = line.split('\t')
		whole_secretome.append(line)
#print(len(whole_secretome[0]))

DE_genes = []
with open('new_DEs_0.05.csv') as DEs:
	for line in DEs:
		line = line.split()
		DE_genes.append(line)
#print(len(DE_genes))

DE_secretome = []
for d in range(0, len(DE_genes)):
	if DE_genes[d][0] in whole_secretome[0]:
		DE_secretome.append(DE_genes[d])

#print(len(DE_secretome))

with open('DE_secretome.csv', 'w') as output:
	output.write('Gene_id'+'\t'+'logFC'+'\t'+'logCPM'+'\t'+'LR'+'\t'+'PValue'+'\n')
	for i in range(0, len(DE_secretome)):
		output.write('\t'.join(DE_secretome[i])+'\n')
