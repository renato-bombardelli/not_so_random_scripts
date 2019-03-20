all_genes = []
with open('predicted_secretome.csv') as predicted:
	for line in predicted:
		line = line.split('\t')
		all_genes.append(line)		

secretome = []
for z in range(0, (len(all_genes)-2)):
	if all_genes[z][6] == 'Y' and all_genes[z][7] == '0' and all_genes[z][8] == 'Not GPI-anchored':
		secretome.append(all_genes[z])

print(secretome)
print(len(secretome))

with open('secretome_only.csv', 'w') as output:
	output.write('line'+'\t'+'Orf'+'\t'+'Start'+'\t'+'End'+'\t'+'Strand'+'\t'+'Introns'+'\t'+'Pep Sinal 4.01c'+'\t'+'PredHel (TMHMM)'+'\t'+'GPI-anchor'+'\t'+'RNAseq cov.(medium)'+'\t'+'RNAseq cov.(200DAI)'+'\t'+'Uniref50 annotation'+'\t'+'nº members'+'\t'+'Lowest common taxon'+'\t'+'Representative member'+'\t'+'rellianum_orf'+'\t'+'Chromosome'+'\t'+'annot'+'\t'+'perc. id'+'\t'+'query coverage'+'\t'+'align lenght'+'\n')
	for d in range(0, len(secretome)):
		output.write('\t'.join(secretome[d]))
