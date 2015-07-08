#Script to do the R part of Dicty genome simulation
#author : Prakhar Gaur
#Date : July 8 IST 2015

#Read data from File, probability values
probVal = read.table("probability-values-codon-usage.txt", header=FALSE)[,1]

#Read data from file, list of Codons (use stringsAsFactors=FALSE, otherwise codons are considered as Factors)
codon = read.table("codon-list.txt", header=FALSE, stringsAsFactors=FALSE)[,1]

#The sample() to generate the sequence, the function gives out one codon which means number of Seq length = nucleotides/3
dictyGenome <-sample(codon,1133333,replace=TRUE, probVal)

#Generate ad save frequency plot of Codons
#png("Condon-usage-freq-plot.png")
#plot(dictyGenome)
#dev.off()

#create string with fasta header
head <- c('>dictyGenome')

# Add fasta header to fasta file
write(head, "dicty-Synthetic-genome.fa")

#Append sequence to fasta file
write.table(paste(dictyGenome,collapse=""), "dicty-Synthetic-genome.fa", append=TRUE, col.name=FALSE, row.name=FALSE, quote=FALSE)

