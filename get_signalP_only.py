with_signalP = []
with open('Full_Ssci_prediction.txt') as predicted:
	for line in predicted:
		line = line.split()
		#print(line)
		try:
			if line[9] in "Y":
				with_signalP.append(line)
		except IndexError:
			continue
print(with_signalP)
print(len(with_signalP))

with open('Ssci_SignalP_only.txt', 'w') as output:
	output.write('# name'+'\t'+'Cmax'+'\t'+'pos'+'\t'+'Ymax'+'\t'+'pos'+'\t'+'Smax'+'\t'+'pos'+'\t'+'Smean'+'\t'+'D'+'\t'+'?'+'\t'+'Dmaxcut'+'\t'+'Networks-used'+'\n')
	for z in range(0, len(with_signalP)):
		output.write('\t'.join(with_signalP[z])+'\n')
