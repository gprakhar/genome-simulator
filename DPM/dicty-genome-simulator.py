#Script to generate simulated genome based on Codon usaage frquency data
#author: prakhar gaur
#date: Tue July 07 IST 2015


import argparse

#argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('lenghtofGenome', metavar='L', default='3400000', help='sequence lenght of the simulated genome in nucleotides, in base pairs (b.p.), default 3400000 b.p.', type=int)
parser.add_argument('-f', '--condonusageTable', help='text file with two columns, Col1 - Codon name, Col2 = Frequency of Codon per thousand, tab seprated, one codon entry per row', type=str)
args = parser.parse_args()

lenght = args.lenghtofGenome #default is assumed to be 3400000 b.p.
frequencyFile = args.condonusageTable


freqDict = {}

with open(frequencyFile, 'r') as inputFilehandle:
	for line in inputFilehandle:
		(key,value) = line.split()
		freqDict[key] = float(value)/1000
		
#print freqDict

with open("out1.txt", "w") as out1, open("out2.txt", "w") as out2:
	for (k,v) in freqDict.items():
		out1.write("%s\n" % k)
		out2.write("%s\n" % str(v))



	
