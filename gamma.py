from __future__ import division

import math
import sys

from nltk.corpus import brown
from nltk import tokenize
import numpy as np

from beta import bestWord, content


def semanticVector(words, jointWords, infoContentNorm):
	wordSet = set(words)
	vector = np.zeros(len(jointWords))
	i = 0
	for jointWord in jointWords:
		if jointWord in wordSet:
			vector[i] = 1
			if infoContentNorm:
				vector[i] = vector[i]*math.pow(content(jointWord), 2)
		else:
			similarWord, similarity =  bestWord(jointWord, wordSet)
			if similarity >0.2:
				vector[i] = 0.2
			else:
				vector[i] = 0.0
			if infoContentNorm:
				vector[i] = vector[i]*content(jointWord)* content(similarWord)
		i+=1
	return vector