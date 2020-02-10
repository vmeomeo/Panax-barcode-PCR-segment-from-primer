import sys
import os

# Make a list of different file name of sequences
f_name = open(r"D:\files\Work\IBT VAST\test\ITS-panax-name.txt")
filename_in = f_name.read().split('\n')
f_name.close()

#a function to avoid error when backslash at the end of string
def createFileLink (filename) :
	name = namestring + filename
	name = name.replace("____","")
	return name

#create string of input file address
namestring = r"D:\files\Work\IBT VAST\test\refseq\____"
filepath_in = []
for item in filename_in :
	filepath_in = filepath_in + [createFileLink(item)]

#create string of output file address
namestring = r"D:\files\Work\IBT VAST\test\refseq\ITS\____"
filepath_out = []
for item in filename_in :
	filepath_out = filepath_out + [createFileLink(item)]

# Short sequences where primers (F, R) ligased with the DNA template
ligateF = 'AGCGGAGGAAAAGAAAC'
ligateR = 'AGGAGAAGTCGTAACAAG'

total_seq = len(filename_in)

#Automatically generate files which consist the DNA sequence we can have after PCR
for item in range(0, total_seq) :
	f_in = open(filepath_in[item],"r")
	fullseq = f_in.read()
	f_in.close()

	f_out = open(filepath_out[item],"w+")

	fullseq = fullseq.replace('\n','')
	indexF = fullseq.find(ligateF)
	indexR = fullseq.find(ligateR)
	lenF = len(ligateF)

	endindex = indexF + lenF #because our NCBI template sequence is an anti-sense strand
	sequence = fullseq[indexR:endindex]

	name = filename_in[item].replace('.fasta','')
	
	f_out.write(">%s\n" %name)
	f_out.write("%s" %sequence)
	f_out.close()
	
	input('Finished!')