# use PYTHON 3
#Script to query web pages at Uniprot and Pfam and download the relevant data
#No proxy handling

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

