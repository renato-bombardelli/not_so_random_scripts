geneID = []
GOterm = []
description = []
with open("Ss_full_GO_annot.csv") as genome:
	for line in genome:
		line = line.split("\t")
		try:
			geneID.append(line[2])
			description.append(line[3])
			GOterm.append(line[9])
		except IndexError:
			continue

for j in range(0, len(GOterm)):
	GOterm[j] = GOterm[j].replace('F:GO', 'GO')
	GOterm[j] = GOterm[j].replace('P:GO', 'GO')
	GOterm[j] = GOterm[j].replace('C:GO', 'GO')

enrichGO = {}
c = 0
while c < len(geneID):

	enrichGO[geneID[c]] = []
	enrichGO[geneID[c]].append(description[c])
	enrichGO[geneID[c]].append(GOterm[c])
	c += 1

print(len(enrichGO))


GOonly = dict( [(k,v) for k,v in enrichGO.items() if len(v[1])>0])
print(GOonly)
print(len(GOonly))

with open("Annotation_file.csv", "w") as output:
	for i in GOonly:
		output.write(i+'\t'+i+'\t'+GOonly[i][0]+'\t'+GOonly[i][1]+'\n')
