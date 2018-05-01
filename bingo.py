#!/usr/bin/python
#
# To do: make number of cards configurable on command line
# Make contents of selection buckets configurable

import re
import os
from appy.pod.renderer import Renderer
import random
import copy
import math

NUMBER_OF_CARDS = 15
# This should normally be the previous year; if not, change the output filename
# at the bottom
YEAR = 2017

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
                'than', 'were', 'who', 'been','an', 'wont', 'dont', 'thru', 
                'could', 'them', 'they', 'myself', 'bu', 'ba', 'da', 'cuz', 
                'off', 'by', 'or', 'o', 'u', 'its', 'aah', 'till', 'yay',
                'love'] # Love is included another way

def process(country, text):
    words = {}
    wordlist = re.split(r"[-\(\)\s\.,\?:!\"]+", text)
    apos = re.compile("\xe2\x80|'|\xc2\xb4");
    ooohhh = re.compile(r"^[oh]+$");
    for word in wordlist:
        word = word.lower()
        # Remove words with apostrophes
        if apos.search(word):
            continue
        # All forms of "ooohhh"
        if ooohhh.search(word):
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

# Print word lists
print "Word lists:"
for i in range(0, len(files) + 1):
    if len(frequency_table[i]):
        print str(i) + ": " + str(frequency_table[i])

# We have five buckets, each of which will fill five squares on any card.
# We fill the buckets with words of different frequencies.
# If you want more of a challenge, add or switch in frequency_table[1],
# which is all the words which only came up once.
orig_buckets = [set(frequency_table[2]),
                set(frequency_table[3]),
                set(frequency_table[4]),
                set(frequency_table[5]),
                set(frequency_table[6]  + frequency_table[7]  +
                    frequency_table[8]  +
                    frequency_table[9]  + frequency_table[10] +
                    frequency_table[11] + frequency_table[12] +
                    frequency_table[13] + frequency_table[14])]

buckets = copy.deepcopy(orig_buckets)

print "\nBucket sizes:"
minsize = 999
for i in range(len(orig_buckets)):
    print len(orig_buckets[i])
    minsize = min(minsize, len(orig_buckets[i]))

def make_card(card_template, buckets):
    
    card = copy.deepcopy(card_template)
    side_length = len(card)    

    # Replenish the stash of words if necessary
    # Refilling at this point prevents duplicates on the same board
    for i in range(side_length):
        if len(buckets[i]) < 5:
            buckets[i] = orig_buckets[i].copy()

    for i in range(side_length):
        for j in range(side_length):
            bucketidx = card[i][j]
            if isinstance(bucketidx, int):

                word = random.sample(buckets[bucketidx], 1)[0]
                card[i][j] = word
                buckets[bucketidx].remove(word)

    # print card
    return card

# This defines which words from which buckets go where; the number is the
# bucket number. "LOVE" is a 'free' square - everyone gets it :-)
# It is arranged so that, to get a line, you have to have spotted a word from
# each bucket, with LOVE counting as bucket 4 (most common).
x = "LOVE"
card_template = [[1, 3, 0, 4, 2],
                 [4, 2, 1, 3, 0],
                 [3, 0, x, 2, 1],
                 [2, 1, 3, 0, 4],
                 [0, 4, 2, 1, 3]]

cards = []            
for i in range(NUMBER_OF_CARDS):
    cards.append(make_card(card_template, buckets))

renderer = Renderer('card-template.odt',
                    globals(),
                    'cards-for-' + str(YEAR + 1) + '.odt')
renderer.run()    
