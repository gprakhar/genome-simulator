#prototype version 1 for the Kinship project
#author: prakhar gaur
#date: Thu July 03 IST 2015

import argparse

#parse arguments and create usage text
parser = argparse.ArgumentParser()
parser.add_argument('keywordfileName', metavar='filename', help='File with comma seprated list of keywords that have to be searched in Uniprot database')
args = parser.parse_args()
inputfileName = args.keywordfileName
