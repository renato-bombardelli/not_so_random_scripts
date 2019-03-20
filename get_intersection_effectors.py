Taniguti = []
with open('effectors_secretoma - LucasLeila.csv') as ssci_pred:
	for line in ssci_pred:
		line = line.split()
		Taniguti.append(line[0])
Taniguti.pop(0)
print(len(Taniguti))

Benevenuto = []
with open('Ssci_effectorP_IDs.csv') as benev:
	for line in benev:
		line = line.split()
		Benevenuto.append(line[0])
print(len(Benevenuto))

intersection = []
for i in range(0, len(Benevenuto)):
	if Benevenuto[i] in Taniguti:
		intersection.append(Benevenuto[i])

print(intersection)

with open('intersection_effectors.csv', 'w') as output:
	output.write('\n'.join(intersection))
