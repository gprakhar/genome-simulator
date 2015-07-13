#script to use Monte Carlo approach on Blast with synthetic genome sequence as databse and DPM protien Human homologs as query
#Author : prakhar gaur
#date : Wed 8 July IST 2015

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('numberofiterations', metavar='N', help='Number of times ti run the Monte carlo simulation', type=int)

args = parser.parse_args()
lenght = args.numberofiterations

#blast binary folder
blastExe = r'/home/littleboy/local_bin/ncbi-blast-2.2.30+/bin/'


for i in range(lenght):
	#generate cmd string for Genome Simulator
	genSynGenome = 'Rscript dicty-genome-simulator.R probability-values-codon-usage.txt codon-list.txt 11333333 %d' % i
	os.system(genSynGenome)

	#replace 'U' in synthetic genome fasta file with 'T'
	with open('dicty-Synthetic-genomeU_%d.fa' % i, 'r') as infile, open('dicty-Synthetic-genome_%d.fa' % i, 'w') as outfile:
    		for line in infile:
			line = line.replace('U', 'T')
			outfile.write(line)

	#delete Synthetic genome file with Uracil
	deleteUfile = 'rm dicty-Synthetic-genomeU_%d.fa' % i
	os.system(deleteUfile)
	
	#generate blast database from Synthetic genome created in previous step
	genSynGenome_blastDB = '%smakeblastdb -in dicty-Synthetic-genome_%d.fa -parse_seqids -dbtype nucl -out dicty-Synthetic-genome_%d' % (blastExe, i, i)
	print genSynGenome_blastDB
	os.system(genSynGenome_blastDB)

	#run blast on the Db created in previous step with DPM protien homologs from humans
	blastcmd = '%stblastn -query DPM-prot.fa -db dicty-Synthetic-genome_%d -out dictySynGenome-blast-out_%d.xml -outfmt 5 -num_threads 23' % (blastExe, i, i)

