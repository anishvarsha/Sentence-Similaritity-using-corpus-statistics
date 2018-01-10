from __future__ import division

import sys
import math
from nltk.corpus import wordnet as wn
from bestSense import bestSense
from compareSynset import PathLength, ScalingDepthEffect


def SemanticSimilarityWords(wordA, wordB):
	bestPair = bestSense(wordA, wordB)
	shortDistance = PathLength(bestPair[0], bestPair[1])
	maxHierarchy = ScalingDepthEffect(bestPair[0], bestPair[1])
	return shortDistance*maxHierarchy