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

#Proxy settings

#http_proxy = "http://proxy.ibab.ac.in:3128/"
#https_proxy = "http://proxy.ibab.ac.in:3128/"
#ftp_proxy = "http://proxy.ibab.ac.in:3128/"

#proxyDict = { 
#              "http"  : http_proxy, 
#              "https" : https_proxy, 
#              "ftp"   : ftp_proxy
#            }

#Read input file with csv module and store it as list
#Line change means new entry
keywordList = list()
with open(inputfileName) as inputfileHandle:
	keywordString = csv.reader(inputfileHandle)
	for row in keywordString:
		keywordList.append(row)

uniprotFastaDl = 'http://www.uniprot.org/uniprot/Q14623.fasta'

##to Download a fasta or similar file or 
for keyword in keywordList:
	uniprotID = ', '.join(map(str, keyword))
	uniprotFastaDl = 'http://www.uniprot.org/uniprot/%s.fasta' % uniprotID
	r = requests.get(uniprotFastaDl, stream=True)#, proxies=proxyDict)
	if r.status_code == 200:
		print r.status_code
		with open("%s.fa" % uniprotID, 'wb') as fileHandle:
		        r.raw.decode_content = True
        		shutil.copyfileobj(r.raw, fileHandle)
	
