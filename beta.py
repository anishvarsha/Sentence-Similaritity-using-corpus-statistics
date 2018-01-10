from __future__ import division

import sys
import math
from nltk.corpus import wordnet as wn
from nltk.corpus import brown
from SemanticWords import SemanticSimilarityWords


wordCount = 0
brownDict = {}

def bestWord(wordA, wordSet):
	similarity = -1.0
	word = ""
	for wordB in wordSet:
		temp = SemanticSimilarityWords(wordA, wordB)
		if temp > similarity:
			similarity = temp
			word = wordB
	return word, similarity


def content(wordData):
	global wordCount
	if wordCount == 0:
		for sent in brown.sents():
			for word in sent:
				key = word.lower()
				#rewrite here
				#if brownDict[key] is None
				if not brownDict.has_key(key):
					brownDict[key] = 0
				brownDict[key]+=1
				wordCount+=1
	wordData = wordData.lower() 
	if not brownDict.has_key(wordData):
		n = 0
	else:
		n = brownDict[wordData]
	
	informationContent = math.log(n+1)/math.log(wordCount+1)
	return 1.0-informationContent