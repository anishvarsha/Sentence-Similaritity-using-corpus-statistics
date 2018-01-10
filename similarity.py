from __future__ import division

import math
import sys

from nltk import word_tokenize as tokenizer

from delta import wordOrder
from gamma import semanticVector
from numpy import dot, linalg


def semanticSimilarity(sentenceA, sentenceB, infoContentNorm):
	wordsA = tokenizer(sentenceA)
	wordsB = tokenizer(sentenceB)
	wordSet = set(wordsA).union(set(wordsB))
	wordVectorA = semanticVector(wordsA, wordSet, infoContentNorm)
	wordVectorB = semanticVector(wordsB, wordSet, infoContentNorm)

	semSimilarity = dot(wordVectorA, wordVectorB)/(linalg.norm(wordVectorA)*linalg.norm(wordVectorB))
	return semSimilarity


def wordSimilarity(sentenceA, sentenceB):
	wordsA = tokenizer(sentenceA)
	wordsB = tokenizer(sentenceB)
	wordSet = list(set(wordsA).union(set(wordsB)))
	index = {word[1]: word[0] for word in enumerate(wordSet)}
	#sr = r1-r2
	r1 = wordOrder(wordsA, wordSet, index)
	r2 = wordOrder(wordsB, wordSet, index)
	srTemp = linalg.norm(r1-r2)/linalg.norm(r1+r2)
	return 1-srTemp


def sentenceSimialrity(sentenceA, sentenceB, infoContentNorm):
	similarity = 0.58 * semanticSimilarity(sentenceA, sentenceB, infoContentNorm) + 0.42* wordSimilarity(sentenceA, sentenceB)
	return similarity