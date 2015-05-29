#Script to query web pages at Uniprot and Pfam and download the relevant data
#No proxy handling
#author: prakhar gaur
#date: Fri Oct 10 10:36:35 IST 2014

import argparse
import csv
import requests

#parse arguments and create usage text
parser = argparse.ArgumentParser()
parser.add_argument('keywordfileName', metavar='filename', help='File with comma seprated list of keywords that have to be searched in Uniprot database')
args = parser.parse_args()
inputfileName = args.keywordfileName

#Read input file with csv module and store it as list
keywordList = list()
with open(inputfileName) as inputfileHandle:
	keywordString = csv.reader(inputfileHandle, dialect='excel')
	for row in keywordString:
		keywordList.append(row)

#Query the Uniprot databse with URL encode queries, one by one from the list of keywords
##URL demo: http://www.uniprot.org/uniprot/?query=gene:wnt AND reviewed:yes AND organism:"Homo sapiens (Human) [9606]"&sort=score&columns=id,entry name,protein names,genes(PREFERRED),organism,length,database(Pfam)

uniprotURL =  r'http://www.uniprot.org/uniprot/query'
uniprotPayload = {'query':'gene:$'


'''
import urllib.request
import shutil
import uniprot

# Download the file from `url` and save it locally under `file_name`:
for i in range(30):
  url = 'http://www.nios.ac.in/media/documents/secscicour/English/Chapter-{0}.pdf'.format(i)
  filename = 'nios_science-technology_chapter{0}.pdf'.format(i)
  print (filename)
  with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
'''
