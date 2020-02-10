import os

rbcL_F = 'ATGTCACCACAAACAGAGACTAAAGC'
rbcL_R = 'TTCGGCACAAAATAAGAAACGATCTC'

#find ligate position
def changeStrand (string):
	string = string.replace('C','M')
	string = string.replace('G','C')
	string = string.replace('M','G')
	string = string.replace('A','M')
	string = string.replace('T','A')
	string = string.replace('M','T')
	return string[::-1]

ligateF = rbcL_F
ligateR = changeStrand (rbcL_R)

# name list of different sequence files
f_name = open(r"D:\files\Work\IBT VAST\test\rbcL-panax-name.txt","r")
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
namestring = r"D:\files\Work\IBT VAST\test\refseq\rbcL\rbcL ____"
filepath_out = []
for item in filename :
	filepath_out = filepath_out + [createFileLink(item)]

total_seq = len(filename)

#Automatically generate files which consist the DNA sequence we can have after PCR
for item in range(0, total_seq) :
	f_in = open(filepath_in[item],"r")
	fullseq = f_in.read()
	f_in.close()

	f_out = open(filepath_out[item],"w+")

	fullseq = fullseq.replace('\n','')

	indexF = fullseq.find(ligateF)
	indexR = fullseq.find(ligateR)
	lenR = len(ligateR)

	endindex = indexR + lenR
	sequence = fullseq[indexF:endindex]

	name = filename[item].replace('.fasta','')

	f_out.write(">%s\n" %name)
	f_out.write("%s" %sequence)
	f_out.close()

	input('Finished!')