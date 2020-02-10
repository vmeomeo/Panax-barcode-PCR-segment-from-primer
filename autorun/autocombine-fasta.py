import os
#namestring = r"D:\files\Work\IBT VAST\Analyse\PCR sequences\ITS\ITS ____"

namecard = ['ITS', 'matK', 'rbcL', 'trnH-psbA']

def createPathColl (collection, namestring, endstring = '') :
	filepath = []
	for item in collection:
		filepath = filepath + [createFileLink(item, namestring, endstring)]
	return filepath

def createFileLink (filename, namestring, endstring = '') :
	name = namestring + filename + endstring
	name = name.replace("____","")
	return name

filepath_getname = createPathColl(namecard, r"D:\files\Work\IBT VAST\test\____","-panax-name.txt")
namestring = r"D:\files\Work\IBT VAST\Analyse\PCR sequences\____"
filepath_out = createPathColl (namecard, namestring, endstring = '.fas')


for item1 in range(0,len(namecard)) :

	f_name = open(filepath_getname[item1],"r")
	filename = f_name.read().split('\n')
	f_name.close()
	
	if (namecard[item1] == 'trnH-psbA'):
		filepath_in = createPathColl (filename, r"D:\files\Work\IBT VAST\Analyse\PCR sequences\trnH-psbA\psbA ____")
	else:
		namestring = r"D:\files\Work\IBT VAST\Analyse\PCR sequences\____" + str(namecard[item1]) + "\____" + str(namecard[item1]) + " "
		filepath_in = createPathColl (filename, namestring)

	total = len(filepath_in)
	
	f_out = open(filepath_out[item1],"w+")

	for item2 in range(0, total):
		f_in = open(filepath_in[item2],"r")
		info = f_in.read()
		f_out.write(info)
		f_out.write('\n')
		f_in.close()

	f_out.close()