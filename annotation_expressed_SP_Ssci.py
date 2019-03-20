###### new annotation with expressed genes only #########
anot = []
with open('Annotation_file.csv') as annotation:
	for line in annotation:
		line = line.split('\t')
		line[3] = line[3].replace('\n', '')
		anot.append(line)

expres = []
with open('new_Expressed_SP_Ssci.csv') as expressed:
	for line in expressed:
		line = line.split()
		expres.append(line)

new_anot = []
c = 0
for d in range(0, len(anot)):
	while c < len(expres):
		if anot[d][0] in expres[c][0]:
			new_anot.append(anot[d][0])
		c += 1
	c = 0

#print(new_anot)
#print(len(new_anot))

#print(anot)

final_list = []
for z in range(0, len(anot)):
	if anot[z][0] in new_anot:
		final_list.append(anot[z])

#print(final_list)
#print(len(final_list))

with open('new_annotation_file_SP_Ssci.csv', 'w') as output:
	for f in range(0, len(final_list)):
		output.write(final_list[f][0]+'\t'+final_list[f][1]+'\t'+final_list[f][2]+'\t'+final_list[f][3]+'\n')
