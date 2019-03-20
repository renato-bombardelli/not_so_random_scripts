
full_list = []
with open("DEs_only_SP_Ssci_FDR.csv") as DEs_005:
	for line in DEs_005:
		line = line.split()
		full_list.append(line)

#print(full_list)

for d in range(1, len(full_list)):

	full_list[d][0] = full_list[d][0].replace('g', '')
	## this is based on the complete S. scitamineum genome chromossomes distribution
	if int(full_list[d][0]) <= 711:
		full_list[d][0] = full_list[d][0]+'_chr01_Ss'
	elif int(full_list[d][0]) <= 1267:
		full_list[d][0] = full_list[d][0]+'_chr02_Ss'
	elif int(full_list[d][0]) <= 1857:
		full_list[d][0] = full_list[d][0]+'_chr03_Ss'
	elif int(full_list[d][0]) <= 2270:
		full_list[d][0] = full_list[d][0]+'_chr04_Ss'
	elif int(full_list[d][0]) <= 2625:
		full_list[d][0] = full_list[d][0]+'_chr05_Ss'
	elif int(full_list[d][0]) <= 2942:
		full_list[d][0] = full_list[d][0]+'_chr06_Ss'
	elif int(full_list[d][0]) <= 3257:
		full_list[d][0] = full_list[d][0]+'_chr07_Ss'
	elif int(full_list[d][0]) <= 3554:
		full_list[d][0] = full_list[d][0]+'_chr08_Ss'
	elif int(full_list[d][0]) <= 3809:
		full_list[d][0] = full_list[d][0]+'_chr09_Ss'
	elif int(full_list[d][0]) <= 4089:
		full_list[d][0] = full_list[d][0]+'_chr10_Ss'
	elif int(full_list[d][0]) <= 4368:
		full_list[d][0] = full_list[d][0]+'_chr11_Ss'
	elif int(full_list[d][0]) <= 4610:
		full_list[d][0] = full_list[d][0]+'_chr12_Ss'
	elif int(full_list[d][0]) <= 4840:
		full_list[d][0] = full_list[d][0]+'_chr13_Ss'
	elif int(full_list[d][0]) <= 5040:
		full_list[d][0] = full_list[d][0]+'_chr14_Ss'
	elif int(full_list[d][0]) <= 5261:
		full_list[d][0] = full_list[d][0]+'_chr15_Ss'
	elif int(full_list[d][0]) <= 5485:
		full_list[d][0] = full_list[d][0]+'_chr16_Ss'
	elif int(full_list[d][0]) <= 5693:
		full_list[d][0] = full_list[d][0]+'_chr17_Ss'
	elif int(full_list[d][0]) <= 5880:
		full_list[d][0] = full_list[d][0]+'_chr18_Ss'
	elif int(full_list[d][0]) <= 6054:
		full_list[d][0] = full_list[d][0]+'_chr19_Ss'
	elif int(full_list[d][0]) <= 6234:
		full_list[d][0] = full_list[d][0]+'_chr20_Ss'
	elif int(full_list[d][0]) <= 6417:
		full_list[d][0] = full_list[d][0]+'_chr21_Ss'
	elif int(full_list[d][0]) <= 6582:
		full_list[d][0] = full_list[d][0]+'_chr22_Ss'
	elif int(full_list[d][0]) <= 6603:
		full_list[d][0] = full_list[d][0]+'_chr26_Ss'
	elif int(full_list[d][0]) <= 6625:
		full_list[d][0] = full_list[d][0]+'_chr24_Ss'
	elif int(full_list[d][0]) <= 6639:
		full_list[d][0] = full_list[d][0]+'_chr25_Ss'
	elif int(full_list[d][0]) <= 6673:
		full_list[d][0] = full_list[d][0]+'_chr23_Ss'

	#print(full_list[d][0])

#print(full_list)

with open('new_DEs_only_SP_Ssci_FDR.csv', 'w') as output:
	for i in range(0, len(full_list)):
		if i == 0:
			output.write(str(full_list[i][0])+'\t'+str(full_list[i][1])+'\t'+str(full_list[i][2])+'\t'+str(full_list[i][3])+'\t'+str(full_list[i][4])+'\t'+str(full_list[i][5])+'\n')			
		else:
			output.write('g'+str(full_list[i][0])+'\t'+str(full_list[i][1])+'\t'+str(full_list[i][2])+'\t'+str(full_list[i][3])+'\t'+str(full_list[i][4])+'\t'+str(full_list[i][5])+'\n')
