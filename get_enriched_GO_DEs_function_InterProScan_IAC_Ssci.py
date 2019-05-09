DE_only = []
LogFC = []
#creates two lists, one containing the gene_ids and another the logFC
with open('new_DEs_only_IAC_Ssci_FDR_0.01.csv') as DE_tags:
	for line in DE_tags:
		line = line.split()
		DE_only.append(line[0])
		LogFC.append(line[1])
#creates a dictionarie linking the gene_id with its logFC
DE_logFC = {}
for z in range(0, len(DE_only)):
	DE_logFC[DE_only[z]] = LogFC[z]

#there is 12 GO categories (for this dataset)
complete = []
GO1 = []

#obtaining the GO categories generated in ermineJ
with open('enriched_GO_IAC_Ssci_0.01.csv') as enriched:
	for line in enriched:
		line = line.split('\t')
		complete.append(line)

#print(complete) #the whole enrichmentGO generate by ermineJ

#create a dictionarie linking gene_id with its function obtained from Blast2GO
linked_id_function = {}
with open('Full_Ssci_annot_InterPro.csv') as annot:
	for line in annot:
		line = line.split('\t')
		linked_id_function[line[2]] = line[3]

##########################################################################################
# Getting the InterProScan information
new_list = []
with open('Sscitamineum_prots.tsv') as interproscan:
	for line in interproscan:
		line = line.split('\t')
		new_list.append(line)

# creating a dictionary linking the gene id with the IPR numbers and Domains [11:13] to pick the columns 11(IPR) and 12(Domain)
inter_dict = {}
for i in range(0, len(new_list)):
	try:
		if new_list[i][0] == new_list[i-1][0]:
			inter_dict[new_list[i][0]] += new_list[i][11:13]
		else:
			inter_dict[new_list[i][0]] = new_list[i][11:13]
	except IndexError:
		continue

#print(inter_dict)

#removing empty items, and line breaks
for k in inter_dict.keys():
	i = 0
	length = len(inter_dict[k])
	while i<length:
		if inter_dict[k][i] == '\n' or inter_dict[k][i] == '':
			inter_dict[k].remove(inter_dict[k][i])
			length -= 1
			continue
		else:
			inter_dict[k][i] = inter_dict[k][i].replace('\n', '')
		i += 1

#removing duplicates (as dictionaries struture don't accept duplicated keys, just convert the list to a dict,
#and go back to list, keeping te order and removing the duplicates)
for k in inter_dict.keys():
	inter_dict[k] = list(dict.fromkeys(inter_dict[k]))

#removing empty lists (ID keys in the dict = [])
newdict = dict([(vkey, vdata) for vkey, vdata in inter_dict.items() if(vdata) ])
#print(newdict)

##########################################################################################

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
		output.write('gene_id'+'\t'+'LogFC'+'\t'+'Function'+'\t'+'InterPro_Accession'+'\t'+'InterPro_Domain'+'\n')
		for k in range(0, len(gene_id)):
			output.write(gene_id[k]+'\t'+logfc[k]+'\t'+linked_id_function[gene_id[k]]+'\t')

			# Get the InterProScan information (Accession and Domain)
			try:
				output.write(newdict[gene_id[k]][0]+'\t'+newdict[gene_id[k]][1]+'\n')
				for j in range(2, len(newdict[gene_id[k]]), 2):
					output.write('\t'*3+newdict[gene_id[k]][j]+'\t'+newdict[gene_id[k]][j+1]+'\n')
			except KeyError:
				continue
	#clears the lists to not interfer in the next GO categorie enriched
	GO1.clear()
	gene_id.clear()
	logfc.clear()
