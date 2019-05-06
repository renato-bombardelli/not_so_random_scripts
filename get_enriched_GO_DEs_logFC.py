DE_only = []
LogFC = []
#creates two lists, one containing the gene_ids and another the logFC
with open('new_DEs_0.05.csv') as DE_tags:
	for line in DE_tags:
		line = line.split()
		DE_only.append(line[0])
		LogFC.append(line[1])
#creates a dictionarie linking the gene_id with its logFC
DE_logFC = {}
for z in range(0, len(DE_only)):
	DE_logFC[DE_only[z]] = LogFC[z]

#there is 11 GO categories (for this dataset)
complete = []
GO1 = []

#obtaining the GO categories generated in ermineJ
with open('enriched_GO.csv') as enriched:
	for line in enriched:
		line = line.split('\t')
		complete.append(line)

print(complete) #the whole enrichmentGO generate by ermineJ

#create a dictionarie linking gene_id with its function obtained from Blast2GO
linked_id_function = {}
with open('Full_Ssci_annot_InterPro.csv') as annot:
	for line in annot:
		line = line.split('\t')
		linked_id_function[line[2]] = line[3]


gene_id = []
logfc = []

for cont in range(1, 13):
	GO1.append(complete[cont])
	GO1[0][11] = GO1[0][11].split('|') #separete to not have conflict in the next steps
	for j in range(0, len(GO1[0][11])):
		if GO1[0][11][j] in DE_logFC:
			gene_id.append(GO1[0][11][j]) #append the genes ID
			#print(GO1[0][11][j]) #Uncomment to verify if it is really the gene ID
			logfc.append(DE_logFC[GO1[0][11][j]]) #append the logFC
			#print(DE_logFC[GO1[0][11][j]]) #Uncomment to verify if it is really the logFC (a float, negative or positive)

	with open(f'{complete[cont][1]}.csv', 'w') as output:
		output.write(GO1[0][0]+'\t'+complete[cont][1]+'\n')
		output.write('gene_id'+'\t'+'LogFC'+'\t'+'Function'+'\n')
		for k in range(0, len(gene_id)):
			output.write(gene_id[k]+'\t'+logfc[k]+'\t'+linked_id_function[gene_id[k]]+'\n')
	#clears the lists to not interfer in the next GO categorie enriched
	GO1.clear()
	gene_id.clear()
	logfc.clear()
