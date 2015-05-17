#!/usr/bin/python
#
# To do: make number of cards configurable on command line
# Make contents of selection buckets configurable

import re
import os
from appy.pod.renderer import Renderer
import random
import copy

NUMBER_OF_CARDS = 15
# This should normally be the previous year; if not, change the output filename
# at the bottom
YEAR = 2014

occurrence_names = {}
frequency_table = []
common_words = ['the', 'to', 'and', 'it', 'i', 'you', 'a', 'of', 'in', 'me',
                'my', 'is', 'for', 'all', 'can', 'on', 'we', 'that', 'so',
                'now', 'like', 'up', 'your', 'one', 'if', 'be', 'have', 'but',
                'with', 'no', 'when', 'from', 'do', 'make', 
                '', 'us', 'what',  'where', 'see', 'will', 'at', 'into',
                'this', 'out', 'why', 'are', 'away', 'go', 'then', 'not', 'our',
                'got', 'only', 'come', 'had', 'was', 'would', 'how',
                'down', 'too', "it's", 'has', 'way', 'am', 'as',
                'than', 'were', 'who', 'been','an',
                'could', 'them', 'they', 'myself',
                'off', 'by']

def process(country, text):
    words = {}
    wordlist = re.split(r"[-\(\)\s\.,\?:!\"]+", text)
    apos = re.compile("\xe2\x80|'|\xc2\xb4");
    for word in wordlist:
        word = word.lower()
        if apos.search(word):
            continue
        
        words[word.lower()] = 1

    for word in words:
        if not word in occurrence_names:
            occurrence_names[word] = []
            
        occurrence_names[word].append(country);

for root, dirs, files in os.walk('lyrics/' + str(YEAR)):
    for filename in files:
        country = filename[:-4]
        
        file = open("lyrics/" + str(YEAR) + "/" + filename, "r");
        text = file.read()
        process(country, text)

# Make a frequency table
frequency_table = [[] for i in range(0, len(files) + 1)]

for word in occurrence_names:
    if word in common_words:
        continue
    
    count = len(occurrence_names[word])
    frequency_table[count].append(word)

print frequency_table
print frequency_table[6]

# We have five buckets, each of which will fill five squares on any card.
# We fill the buckets with words of different frequencies. 
buckets = [frequency_table[2],
           frequency_table[3],
           frequency_table[4],
           frequency_table[5] + frequency_table[6],
           frequency_table[7] + frequency_table[8] + frequency_table[9]]

def make_card(card_template, buckets):
    card = copy.deepcopy(card_template)
    
    side_length = len(card)    
    cardwords = []
    
    for i in range(side_length):
        cardwords.append(random.sample(set(buckets[i]), side_length))

    for i in range(side_length):
        for j in range(side_length):
            setidx = card[i][j]
            if isinstance(setidx, int):
                card[i][j] = cardwords[setidx - 1][i]

    # print card
    return card

# This defines which words from which buckets go where; the number is the
# bucket number. "LOVE" is a 'free' square - everyone gets it :-)
# It is arranged so that, to get a line, you have to have spotted a word from
# each bucket. (With LOVE counting as bucket 5, most common.)
card_template = [[2, 4, 1, 5, 3],
                 [5, 3, 2, 4, 1],
                 [4, 1, "LOVE", 3, 2],
                 [3, 2, 4, 1, 5],
                 [1, 5, 3, 2, 4]]

cards = []            
for i in range(NUMBER_OF_CARDS):
    cards.append(make_card(card_template, buckets))

renderer = Renderer('card-template.odt',
                    globals(),
                    'cards-for-' + str(YEAR + 1) + '.odt')
renderer.run()    
