#Script to query web pages at Uniprot and Pfam and download the relevant data
#No proxy handling
#author: prakhar gaur
#date: Fri Oct 10 10:36:35 IST 2014

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
keywordList = list()
with open(inputfileName) as inputfileHandle:
	keywordString = csv.reader(inputfileHandle, dialect='excel')
	for row in keywordString:
		keywordList.append(row)

#Query the Uniprot databse with URL encode queries, one by one from the list of keywords
##URL demo: http://www.uniprot.org/uniprot/?query=gene:wnt AND reviewed:yes AND organism:"Homo sapiens (Human) [9606]"&sort=score&columns=id,entry name,protein names,genes(PREFERRED),organism,length,database(Pfam)

#download-->#http://www.uniprot.org/uniprot/?sort=score&desc=&compress=yes&query=gene:wnt%20AND%20reviewed:yes%20AND%20organism:%22Homo%20sapiens%20(Human)%20[9606]%22&fil=&format=fasta&force=yes
uniprotDlURL = 'http://www.uniprot.org/uniprot/?sort=score&desc=&compress=yes&query=gene:wnt%20AND%20reviewed:yes%20AND%20organism:%22Homo%20sapiens%20(Human)%20[9606]%22&fil=&format=fasta&force=yes'

#1column-query#download it- gunziped #http://www.uniprot.org/uniprot/?sort=&desc=&compress=yes&query=family:%22wnt%20family%22&fil=organism:%22Homo%20sapiens%20(Human)%20[9606]%22%20AND%20reviewed:yes&format=tab&force=yes&columns=id
uniprotQURL = 'http://www.uniprot.org/uniprot/?sort=&desc=&compress=yes&query=family:%22wnt%20family%22&fil=organism:%22Homo%20sapiens%20(Human)%20[9606]%22%20AND%20reviewed:yes&format=tab&force=yes&columns=id'
#uniprotPayload = {'gene': 'wnt', 'reviewed': 'yes', 'organism': '"Homo sapiens (Human) [9606]"', 'sort': 'score', 'columns[]': ['id', 'entry name', 'protein names', 'genes(PREFERRED)', 'organism', 'length', 'database(Pfam)']}

#r = requests.get(uniprotQURL)
#print r.encoding
#print r.text



##to Download a fasta or similar file
r = requests.get(uniprotQURL, stream=True)
if r.status_code == 200:
	print r.status_code
	with open("reply.list.gz", 'wb') as fileHandle:
	        r.raw.decode_content = True
        	shutil.copyfileobj(r.raw, fileHandle) 

