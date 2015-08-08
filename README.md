# CHG-projects
## Beta version of the genome simulator
##Author : Prakhar Gaur
##Date : 21 July 2015

The pipeline is to be re-designed. 
Features:
1. the code will generate random nucleotide sequence based on the nucleotide content of the D. discoideum genome
	size (S) should be, S = Gs (genome size) - Gg (Gene content)
2. generate according to the Dictybase gff, simulated genes of size, the Codon usage table to be used here
3. Insert the simulated genes at locations as per Dictybase gff file



##Old version below

Code base for Genome simulator
This pipeline has been written in R and Python.
It takes as input a codon usage frequency file and a file with Nucleotide content of genome and lenght of genome and a gff file with list of genes 

Using the data from the two input files it generates a simulated genome, contrained by the parameters of the input files
