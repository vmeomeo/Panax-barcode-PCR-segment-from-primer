import os

#different cases when PCR matK sequences
psbA_F = 'ACAAATGGATAAGACCCGGTCT'
psbA_R = 'ATCCACTTGGCTACATCCGC'
psbA_F_A1 = 'ACAAATGGATAAGACCCAGTCT'
psbA_F_A2 = 'ACAAATGGATAAGACCCGATCT'

#find ligate position
def changeStrand (string):
	string = string.replace('C','M')
	string = string.replace('G','C')
	string = string.replace('M','G')
	string = string.replace('A','M')
	string = string.replace('T','A')
	string = string.replace('M','T')
	return string[::-1]

ligate_F = changeStrand (psbA_F)
ligate_F_A1 = changeStrand (psbA_F_A1)
ligate_F_A2 = changeStrand (psbA_F_A2)
ligate_R = psbA_R

#tag file to categorize different sequences into 2 ligating cases
f_tag = open(r"D:\files\Work\IBT VAST\test\trnH-psbA-panax-name_tag.txt","r")
tagfile = f_tag.read().split('\n')
f_tag.close()

# name list of different sequence files
f_name = open(r"D:\files\Work\IBT VAST\test\trnH-psbA-panax-name.txt","r")
filename = f_name.read().split('\n')
f_name.close()

#a function to avoid error when backslash at the end of string
def createFileLink (filename) :
	name = namestring + filename
	name = name.replace("____","")
	return name

#create string of input file address
namestring = r"D:\files\Work\IBT VAST\test\refseq\____"
filepath_in = []
for item in filename :
	filepath_in = filepath_in + [createFileLink(item)]

#create string of output file address
namestring = r"D:\files\Work\IBT VAST\test\refseq\trnH-psbA\psbA ____"
filepath_out = []
for item in filename :
	filepath_out = filepath_out + [createFileLink(item)]

total_seq = len(tagfile)

#Automatically generate files which consist the DNA sequence we can have after PCR
for item in range(0, total_seq) :
	f_in = open(filepath_in[item],"r")
	fullseq = f_in.read()
	f_in.close()

	f_out = open(filepath_out[item],"w+")

	fullseq = fullseq.replace('\n','')

	if (tagfile[item] == 'z'):
		ligateF = ligate_F

	if (tagfile[item] == 'a1'):
		ligateF = ligate_F_A1

	if (tagfile[item] == 'a2'):
		ligateF = ligate_F_A2

	ligateR = ligate_R

	indexF = fullseq.find(ligateF)
	indexR = fullseq.find(ligateR)
	lenF = len(ligateF)

	endindex = indexF + lenF
	sequence = fullseq[indexR:endindex]

	name = filename[item].replace('.fasta','')

	f_out.write(">%s\n" %name)
	f_out.write("%s" %sequence)
	f_out.close()

	input('Finished!')