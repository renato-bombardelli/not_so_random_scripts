effectors = []
with open('predicted_effetor_secretome.txt') as predicted:
	for line in predicted:
		line = line.split()
		try:
			if line[1] == "Effector" and line not in effectors:
				effectors.append(line)
		except IndexError:
			continue

high_probability = []

for z in range(0, len(effectors)):
	try:
		if float(effectors[z][2]) > 0:
			high_probability.append(effectors[z])
	except ValueError:
		continue
print(f'{len(high_probability)} predicted effectors')

with open('Effector_only.txt', 'w') as output:
	output.write('Identifier'+'\t'+'Prediction'+'\t'+'Probability'+'\n')
	for i in range(0, len(high_probability)):
		output.write(high_probability[i][0]+'\t'+high_probability[i][1]+'\t'+high_probability[i][2]+'\n')
