intersection_effectors = []
with open('intersection_effectors.csv') as intersec:
	for line in intersec:
		line = line.split()
		intersection_effectors.append(line[0])

#print(len(intersection_effectors))

DE_genes = []
with open('new_DEs_0.05.csv') as DEs:
	for line in DEs:
		line = line.split()
		DE_genes.append(line[0])
#print(len(DE_genes))

DE_effectors = []
for i in range(0, len(DE_genes)):
	if DE_genes[i] in intersection_effectors:
		DE_effectors.append(DE_genes[i])

print(DE_effectors)

with open('DE_effectors_intersec_Taniguti_Benevenuto.txt', 'w') as output:
	output.write('\n'.join(DE_effectors))