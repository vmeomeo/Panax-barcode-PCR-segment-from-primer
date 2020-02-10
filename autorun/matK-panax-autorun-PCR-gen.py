import os

#different cases when PCR matK sequences
matK_F0 = 'CGATCTATTCATTCAATATTTC'
matK_R = 'GTTCTAGCACAAGAAAGTCG'
matK_F_A = 'CGATCAATTCATTCAATATTTC'
matK_F_AG = 'CGATCAATTCATTCGATATTTC'

#find ligate position
def changeStrand (string):
	string = string.replace('C','M')
	string = string.replace('G','C')
	string = string.replace('M','G')
	string = string.replace('A','M')
	string = string.replace('T','A')
	string = string.replace('M','T')
	return string[::-1]

ligate_F0 = changeStrand (matK_F0)
ligate_F_A = changeStrand (matK_F_A)
ligate_F_AG = changeStrand (matK_F_AG)

#tag file to categorize different sequences into 2 ligating cases
f_tag = open(r"D:\files\Work\IBT VAST\test\matK-panax-name_tag.txt","r")
tagfile = f_tag.read().split('\n')

# name list of different sequence files
f_name = open(r"D:\files\Work\IBT VAST\test\matK-panax-name.txt","r")
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

#another way is:
#namestring = r'D:\files\Work\IBT VAST\test\refseq'
#filepath_in = []
#for item in filename :
#	filepath_in += [os.path.join(namestring, item)]

#create string of output file address
namestring = r"D:\files\Work\IBT VAST\test\refseq\matK\matK ____"
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

	if (tagfile[item] == 'a'):
		ligateF = ligate_F_A

	if (tagfile[item] == 'ag'):
		ligateF = ligate_F_AG

	ligateR = matK_R

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