from __future__ import division

import sys

from nltk.corpus import wordnet as wn


def bestSense(wordA, wordB):
	similarity = -1.0
	synsetsWordA = wn.synsets(wordA)
	synsetsWordB = wn.synsets(wordB)

	if len(synsetsWordA) == 0 or len(synsetsWordB) == 0:
		return None, None

	else:
		similarity = -1.0
		bestPair = None, None

		for synsetWordA in synsetsWordA:
			for synsetWordB in synsetsWordB:
				temp = wn.path_similarity(synsetWordA, synsetWordB)
				if temp > similarity:
					similarity = temp
					bestPair = synsetWordA, synsetWordB
		return bestPair

