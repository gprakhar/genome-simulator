#Script that use the Biopython way of creating Random simulated genomes out of real genomes
##Author : Prakhar Gaur
##Date : 18 Aug 2015

import random
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('genomeFilename', metavar='f', help='name of genome file in fasta format')
parser.add_argument('numTimes', metavar='n', help='number of randomized genomes to generate')

args = parser.parse_args()
inputfileName = str(args.genomeFilename)
num = int(args.numTimes)

def make_shuffle_record(record, new_id):
    nuc_list = list(record.seq)
    random.shuffle(nuc_list)
    return SeqRecord(Seq("".join(nuc_list), record.seq.alphabet), \
           id=new_id, description="Based on %s" % original_rec.id)

original_rec = SeqIO.read(inputfileName,"fasta")
shuffled_recs = (make_shuffle_record(original_rec, "Shuffled%i" % (i+1)) \
                 for i in range(num))
handle = open("shuffled.fasta", "w")
SeqIO.write(shuffled_recs, handle, "fasta")
handle.close()
