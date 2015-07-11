#script to use Monte Carlo approach on Blast with synthetic genome sequence as databse and DPM protien Human homologs as query
#Author : prakhar gaur
#date : Wed 8 July IST 2015

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('numberofiterations', metavar='N', help='Number of times ti run the Monte carlo simulation', type=int)

args = parser.parse_args()
lenght = args.numberofiterations

for i in range(lenght):

