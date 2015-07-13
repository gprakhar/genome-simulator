#Script to generate two files from Codon usage frquency data, one file has probability values and other Codon names
#author: prakhar gaur
#date: Tue July 07 IST 2015


import argparse

#argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--condonusageTable', help='text file with two columns, Col1 - Codon name, Col2 = Frequency of Codon per thousand, tab seprated, one codon entry per row', type=str)
args = parser.parse_args()

frequencyFile = args.condonusageTable

freqDict = {}

with open(frequencyFile, 'r') as inputFilehandle:
	for line in inputFilehandle:
		(key,value) = line.split()
		freqDict[key] = float(value)/1000
		
#print freqDict

with open("codon-list.txt", "w") as out1, open("probability-values-codon-usage.txt", "w") as out2:
	for (k,v) in freqDict.items():
		out1.write("%s\n" % k)
		out2.write("%s\n" % str(v))



	
