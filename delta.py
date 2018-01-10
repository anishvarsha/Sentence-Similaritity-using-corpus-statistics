from __future__ import division

import math
import sys

from nltk.corpus import brown
from nltk import tokenize
import numpy as np
from beta import bestWord


def wordOrder(words, jointWords, index):
	vector = np.zeros(len(jointWords))
	i = 0
	wordSet = set(words)
	for jointWord in jointWords:
		if jointWord in wordSet:
			vector[i] = index[jointWord]
		else:
			wordSimilar, similarity = bestWord(jointWord, wordSet)
			if similarity > 0.4:
				vector[i] = index[wordSimilar]
			else:
				vector[i] = 0
		i +=1
	return vector


