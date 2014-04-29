from __future__ import division
import operator
import math
from collection import *
from nlp import *
from collections import OrderedDict
import collections

#set the subdirectory where the module will search for files
sub_dir="library"
query="heard that the Osmington school"
print ''
print 'The query is "',query,'"'
query = nlp(query)

list_of_terms = {}
total_documents = 0
inverse_term_freq = {}
tfidf_scores = {}

#collect all the filenames
list_of_filenames = findall(sub_dir)
# print list_of_filenames
total_documents=len(list_of_filenames)

#assign them ids
ids=assignids(list_of_filenames)
# print ids	

for filename in list_of_filenames:
	data = getDocument(filename,sub_dir)
	# print data
	nlp_list = nlp(data)
	for term in nlp_list:
		if list_of_terms.has_key(term):
			if list_of_terms[term].has_key(ids[filename]):
				list_of_terms[term][ids[filename]]=list_of_terms[term][ids[filename]]+1
			else:
				list_of_terms[term].update({ids[filename]:1})
		else:
			list_of_terms.update({term:{ids[filename]:1}})

'''
list_of_terms now is a dictionary which contains term frequencies in the documents
the format for the same is :
{term:{docID:frequency}}
'''
for term, value in list_of_terms.iteritems():
	for docID,frequency in value.iteritems():
		inside = float(total_documents/frequency)
		idf_value=math.log10(1+inside)
		tfidf = idf_value*frequency
		if inverse_term_freq.has_key(term):
			if inverse_term_freq[term].has_key(docID):
				inverse_term_freq[term][docID]=idf_value
				tfidf_scores[term][docID]=tfidf
			else:
				inverse_term_freq[term].update({docID:idf_value})
				tfidf_scores[term].update({docID:tfidf})
		else:
			inverse_term_freq.update({term:{docID:idf_value}})
			tfidf_scores.update({term:{docID:tfidf}})

# print tfidf_scores

'''
have to score the documents based on the query
'''

scores = {}
for filename in list_of_filenames:
	scores.update({ids[filename]:0})

for word in query:
	if tfidf_scores.has_key(word):
		for docID, tf_value in tfidf_scores[word].iteritems():
			scores[docID]+=tf_value

sorted_scores = OrderedDict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print ''
print "Displaying results in relevance order"
for docID, score in sorted_scores.iteritems():
	print getFilenameById(docID,ids)," : ",score