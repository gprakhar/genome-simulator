#Script to generate random genome sequence according to Nucleotide content data from D. dicoideum genome
#author : Prakhar Gaur
#Date : August 8 IST 2015

args <- commandArgs(trailingOnly = TRUE)

if(length(args) < 4)
{
  stop("Usage: Rscript dicty-genome-simulator.R <Probability score file> <Nucleotide name file> <Number of Nucleotides> <iteration count>")
}

#Read Nucleotide content data from file, probability values
probVal = read.table(args[1], header=FALSE)[,1]

#Read data from file, list of Nucleotides (A,T,G,C) (use stringsAsFactors=FALSE, otherwise nucleotides are considered as Factors)
nulc = read.table(args[2], header=FALSE, stringsAsFactors=FALSE)[,1]

#The sample() to generate the sequence, the function gives out codons which means number of Seq length = nucleotides/3, genome size
numberofNulc = as.numeric(args[3])
dictyGenome <-sample(nulc,numberofNulc,replace=TRUE, probVal)

#create string with fasta header
iterationFlag = as.numeric(args[4])
head = sprintf(">dictySynGenome-%d", iterationFlag)

# Add fasta header to fasta file
genomeFilename = sprintf("dicty-Synthetic-genomeU_%d.fa", iterationFlag)
write(head, genomeFilename)

#Append sequence to fasta file
write.table(paste(dictyGenome,collapse=""), genomeFilename, append=TRUE, col.name=FALSE, row.name=FALSE, quote=FALSE)

