#Script to query web pages at Uniprot and Pfam and download the relevant data
#No proxy handling
#author: prakhar gaur
#date: Thu May 28 IST 2015

import argparse
import csv
import requests
import shutil

#parse arguments and create usage text
parser = argparse.ArgumentParser()
parser.add_argument('keywordfileName', metavar='filename', help='File with comma seprated list of keywords that have to be searched in Uniprot database')
args = parser.parse_args()
inputfileName = args.keywordfileName

#Read input file with csv module and store it as list
#Line change means new entry
keywordList = list()
with open(inputfileName) as inputfileHandle:
	keywordString = csv.reader(inputfileHandle)
	for row in keywordString:
		keywordList.append(row)

uniprotURL-fasta = 'http://www.uniprot.org/uniprot/?sort=score&desc=&compress=yes&query=gene:wnt%20AND%20reviewed:yes%20AND%20organism:%22Homo%20sapiens%20(Human)%20[9606]%22&fil=&format=fasta&force=yes'

#1column-query- list of Uniprot id's #download it- gunziped #http://www.uniprot.org/uniprot/?sort=&desc=&compress=yes&query=family:%22wnt%20family%22&fil=organism:%22Homo%20sapiens%20(Human)%20[9606]%22%20AND%20reviewed:yes&format=tab&force=yes&columns=id
uniprotQURL = 'http://www.uniprot.org/uniprot/?sort=&desc=&compress=yes&query=family:wnt&fil=organism:%22Homo%20sapiens%20(Human)%20[9606]%22%20AND%20reviewed:yes&format=tab&force=yes&columns=id'

for keyword in keywordList:
	uniprotQURL = 'http://www.uniprot.org/uniprot/?sort=&desc=&compress=yes&query=family:%d&fil=organism:%22Homo%20sapiens%20(Human)%20[9606]%22%20AND%20reviewed:yes&format=tab&force=yes&columns=id' % keyword
	print uniprotQURL

##to Download a fasta or similar file or 
##
r = requests.get(uniprotQURL, stream=True)
if r.status_code == 200:
	print r.status_code
	with open("reply.list.gz", 'wb') as fileHandle:
	        r.raw.decode_content = True
        	shutil.copyfileobj(r.raw, fileHandle) 

	
