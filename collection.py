'''
Read filenames in the library folder
'''

import os
#finds all the documents in the folder specified
def findall():	
	files = []
	for file in os.listdir("./library"):
	    if file.endswith(".txt"):
	    	files.append(file)
	return files

#assigns numeric ids to all the documents
def assignids(files):
	x=1;
	ids = {}
	for filename in files:
		ids[x]=filename
		x=x+1
	return ids