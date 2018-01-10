from similarity import sentenceSimialrity
from bestSense import bestSense 

from SemanticWords import SemanticSimilarityWords
word_pairs = [
  ["asylum", "fruit", 0.21],
  ["autograph", "shore", 0.29],
  ["autograph", "signature", 0.55],
  ["automobile", "car", 0.64],
  ["bird", "woodland", 0.33],
  ["boy", "rooster", 0.53],
  ["boy", "lad", 0.66],
  ["boy", "sage", 0.51],
  ["cemetery", "graveyard", 0.73],
  ["coast", "forest", 0.36],
  ["coast", "shore", 0.76],
  ["cock", "rooster", 1.00],
  ["cord", "smile", 0.33],
  ["cord", "string", 0.68],
  ["cushion", "pillow", 0.66],
  ["forest", "graveyard", 0.55],
  ["forest", "woodland", 0.70],
  ["furnace", "stove", 0.72],
  ["glass", "tumbler", 0.65],
  ["grin", "smile", 0.49],
  ["gem", "jewel", 0.83],
  ["hill", "woodland", 0.59],
  ["hill", "mound", 0.74],
  ["implement", "tool", 0.75],
  ["journey", "voyage", 0.52],
  ["magician", "oracle", 0.44],
  ["magician", "wizard", 0.65],
  ["midday", "noon", 1.0],
  ["oracle", "sage", 0.43],
  ["serf", "slave", 0.39]
]
for word_pair in word_pairs:
    print "%s\t%s\t%.2f\t%.2f" % (word_pair[0], word_pair[1], word_pair[2], 
                                  SemanticSimilarityWords(word_pair[0], word_pair[1]))
sentence_pairs = [
    ["I like that bachelor.", "I like that unmarried man.", 0.561],
    ["Red alcoholic drink.", "A bottle of wine.", 0.585],
    ["I have a hammer.", "Take some nails.", 0.508],
    ["John is very nice.", "Is John very nice?", 0.977],
    ["It is a dog.", "It is a log.", 0.623],
    ["Red alcoholic drink.", "An English dictionary.", 0.0],
    ["Dogs are animals.", "They are common pets.", 0.738],
    ["Canis familiaris are animals.", "Dogs are common pets.", 0.362],
    ["A glass of cider.", "A full cup of apple juice.", 0.678],
    ["I have a hammer.", "Take some apples.", 0.121],
    ["It is a dog.", "It is a pig.", 0.790],
    ["I have a pen.", "Where is ink?", 0.129],
    ["I have a pen.", "Where do you live?", 0.0],
    ["Red alcoholic drink.", "Fresh orange juice.", 0.611],
    
    ["Red alcoholic drink.", "Fresh apple juice.", 0.420],
    
    ["It is a dog.", "That must be your dog.", 0.739],
    
    
    
    
    
    
    
    
]
for sent_pair in sentence_pairs:
    print "%s\t%s\t%.3f\t%.3f\t%.3f" % (sent_pair[0], sent_pair[1], sent_pair[2], 
        sentenceSimialrity(sent_pair[0], sent_pair[1], False),
        sentenceSimialrity(sent_pair[0], sent_pair[1], True))