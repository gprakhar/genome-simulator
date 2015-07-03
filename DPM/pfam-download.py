#Script to query web pages Pfam and download the relevant data
#No proxy handling
#author: prakhar gaur
#date: Thu JULY 3 IST 2015

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
	keywordList = [keyword.strip('\n') for keyword in inputfileHandle.readlines()]
	
##to Download a HMM or similar file or 
##
pfamDL = r'http://pfam.xfam.org/family/%s/hmm'

for keyword in keywordList:
	pfamID = keyword
	url = 'http://pfam.xfam.org/family/%s/hmm' % pfamID
	r = requests.get(url, stream=True)#, proxies=proxyDict)
	if r.status_code == 200:
		print r.status_code
		with open("%s.hmm" % pfamID, 'wb') as fileHandle:
		        r.raw.decode_content = True
        		shutil.copyfileobj(r.raw, fileHandle)
	
