DE_only = []
LogFC = []
with open('new_DEs_0.01.csv') as DE_tags:
	for line in DE_tags:
		line = line.split()
		DE_only.append(line[0])
		LogFC.append(line[1])

DE_logFC = {}
for z in range(0, len(DE_only)):
	DE_logFC[DE_only[z]] = LogFC[z]

#there is 11 GO categories
complete = []
GO1 = []

with open('enriched_GO_001.csv') as enriched:
	for line in enriched:
		line = line.split('\t')
		complete.append(line)

print(complete)

gene_id = []
logfc = []

for cont in range(1, 12):
	GO1.append(complete[cont])
	GO1[0][11] = GO1[0][11].split('|')
	for j in range(0, len(GO1[0][11])):
		if GO1[0][11][j] in DE_logFC:
			gene_id.append(GO1[0][11][j])
			logfc.append(DE_logFC[GO1[0][11][j]])

	with open(f'{complete[cont][1]}.csv', 'w') as output:
		output.write(GO1[0][0]+'\t'+complete[cont][1]+'\n')
		output.write('gene_id'+'\t'+'LogFC'+'\n')
		for k in range(0, len(gene_id)):
			output.write(gene_id[k]+'\t'+logfc[k]+'\n')
	GO1.clear()
	gene_id.clear()
	logfc.clear()
