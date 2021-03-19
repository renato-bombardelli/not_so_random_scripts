dic = {}
ident_cutoff = 70
qcov_cutoff = 80
with open("Uhor_Sreil_BlastP.tsv") as inp:
	for line in inp:
		if line[0][0] != '#':
			line = line.split('\t')
			line[15] = line[15].replace('\n', '')
			#line[2] = %ident
			#line[12] = %qcov
			try:
				if float(dic[line[0]][2]) < float(line[2]) and float(line[12]) >= qcov_cutoff:
					dic[line[0]] = line
			except KeyError:
				if float(line[2]) >= ident_cutoff and float(line[12]) >= qcov_cutoff:
					dic[line[0]] = line
			except IndexError:
				continue

#print(dic)
#print(len(dic))

with open('./best_hits/Uhor_Sreil_best-hits.tsv', 'w') as out:
	out.write('query\tsubject\t%ident\talingment_length\tmismatches\tgap_opens\tqstart\tqend\tsstart\tsend\tevalue\tbit_score\t%qcoverage\tqlength\tslength\tstitle\n')
	for i in dic.items():
		out.write('\t'.join(i[1])+'\n')
