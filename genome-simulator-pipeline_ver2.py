#script to work as the pipeline for running the 
#Author : prakhar gaur
#date : Tue 21 July IST 2015

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('numberofiterations', metavar='N', help='Number of times to run the Monte carlo simulation', type=int)
parser.add_argument('codonfreqfile', metavar='C', help='text file with two columns, Col1 - Codon name, Col2 = Frequency of Codon per thousand, tab seprated, one codon entry per row')

args = parser.parse_args()
lenght = args.numberofiterations
codonFreqFile = str(args.codonfreqfile)

for i in range(lenght):
	#run parsing script to read frequency values and write them as Codon usage probability to seprate file 
	parseCodonFreqFile = 'python dicty-codon-usage-file_parser.py -f %s' % codonFreqFile
	os.system(parseCodonFreqFile)
	
	#Run the R script to generate the simulated gneome, using a sample() with replace
	genSynGenome = 'Rscript dicty-genome-simulator.R probability-values-codon-usage.txt codon-list.txt 11333333 %d' % i #generate cmd string for Genome Simulator
	os.system(genSynGenome)

	#replace 'U' in synthetic genome fasta file with 'T'
	with open('dicty-Synthetic-genomeU_%d.fa' % i, 'r') as infile, open('dicty-Synthetic-genome_%d.fa' % i, 'w') as outfile:
    		for line in infile:
			line = line.replace('U', 'T')
			outfile.write(line)
