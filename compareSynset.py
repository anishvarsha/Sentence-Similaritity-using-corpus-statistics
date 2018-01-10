from __future__ import division

import sys
import math
from nltk.corpus import wordnet as wn

#3.1.2 contribute path length
def PathLength(synsetA, synsetB):
	maxLength = sys.maxint
	if synsetA is None or synsetB is None:
		return 0.0
	if synsetA == synsetB:
		maxLength = 0.0
	else:
		lemmaSetA = set([str(word.name()) for word in synsetA.lemmas()])
		lemmaSetB = set([str(word.name()) for word in synsetB.lemmas()])
		#this line if the word is none
		if len(lemmaSetA.intersection(lemmaSetB)) > 0:
			maxLength = 1.0
		else:
			maxLength = synsetA.shortest_path_distance(synsetB)
			if maxLength is None:
				maxLength = 0.0
			
	shortDistance = math.exp(-0.2*maxLength)
	return shortDistance

def ScalingDepthEffect(synsetA, synsetB):
	maxLength = sys.maxint
	smoothingFactor = 0.45
	if synsetA is None or synsetB is None:
		return maxLength

	if synsetA == synsetB:
		maxLength = max(word[1] for word in synsetA.hypernym_distances())

	else:
		hypernymWordA = {word[0]: word[1] for word in synsetA.hypernym_distances()}
		hypernymWordB = {word[0]: word[1] for word in synsetB.hypernym_distances()}
		commonValue = set(hypernymWordA.keys()).intersection(set(hypernymWordB.keys()))
		if len(commonValue) <=0:
			maxLength = 0
		else:
			distances = []
			for common in commonValue:
				commonWordADist = 0
				commonWordBDist = 0
				if hypernymWordA.has_key(common):
					commonWordADist = hypernymWordA[common]
				if hypernymWordB.has_key(common):
					commonWordBDist = hypernymWordB[common]
				maxDistance = max(commonWordADist, commonWordBDist)
				distances.append(maxDistance)
			maxLength = max(distances)
	treeDist = (math.exp(smoothingFactor*maxLength)- math.exp(-smoothingFactor*maxLength))/(math.exp(smoothingFactor*maxLength) + math.exp(-smoothingFactor*maxLength))

	return treeDist