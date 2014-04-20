'''
Read filenames in the library folder
'''

import os
#finds all the documents in the folder specified
def findall(sub_dir):	
	files = []
	for file in os.listdir("./"+sub_dir):
	    if file.endswith(".txt"):
	    	files.append(file)
	return files

#assigns numeric ids to all the documents
def assignids(files):
	x=1;
	ids = {}
	for filename in files:
		ids[filename]=x
		x=x+1
	return ids

def getDocument(filename,sub_dir):
	with open (os.path.join(sub_dir, filename), "r") as myfile:
		data=myfile.read().replace('\n', '')
	return data

def getFilenameById(search_id,dict):
	for filename, assignedID in dict.iteritems():
	    if search_id == assignedID:
	        return filename