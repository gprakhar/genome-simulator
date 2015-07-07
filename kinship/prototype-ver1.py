#prototype version 1 for the Kinship project
#author: prakhar gaur
#date: Thu July 03 IST 2015

import argparse

#parse arguments and create usage text
parser = argparse.ArgumentParser()
parser.add_argument('numberofgenerations', metavar='numGen', default='10', type=int, help='Number of progeny generations that have to be simulated')
parser.add_argument('numberofalleles', metavar='numAlleles', default='1', type=int, help='Number of Alleles for simulatiom')
parser.add_argument('numberofchromosomes', metavar='numChr', default='1', type=int, help='Number of Chromosomes')

args = parser.parse_args()
numGen = args.numberofgenerations
numAlleles = args.numberofalleles
numChr = args.numberofchromosomes

print "Gen=%d Alleles=%d Chr=%d" % (numGen, numAlleles, numChr)


