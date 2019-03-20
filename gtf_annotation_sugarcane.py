seqname = []
seq_length = []

with open("annotation_sugarcane_comps_GGs.csv") as anot_cana:
	for line in anot_cana:
		line = line.split(";")
		seqname.append(line[0])
		seq_length.append(line[4])

seqname.pop(0)
seq_length.pop(0)

#print(seqname)
#print(len(seqname))

#print(seq_length)
#print(len(seq_length))

with open("annotation_sugarcane.gtf", "w") as output:
	for i in range(0, len(seqname)):
		output.write(seqname[i]+'\t'+'comps_GGs'+'\t'+'exon'+'\t'+'1'+'\t'+seq_length[i]+'\t'+'.'+'\t'+'.'+'\t'+'0'+'\t'+'transcript_id '+'\"'+seqname[i]+'.t1'+'\"'+'; '+'gene_id '+'\"'+seqname[i]+'\"'+';'+'\n')