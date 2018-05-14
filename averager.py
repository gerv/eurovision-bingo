#!/usr/bin/python
#
# This code calculates average frequencies across a set of years of lyrics,
# to enable words to be manually chosen for the "any year" cards.

import re
import os
import random
import copy
import math

# total_occurrence_count = word -> count across all years
total_occurrence_count = {}

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

def process(occurrence_names, country, text):
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

    return occurrence_names


years = (2013, 2014, 2015, 1016, 2017)
for year in years:
    occurrence_names = {}
    
    for root, dirs, files in os.walk('lyrics/' + str(year)):
        for filename in files:
            country = filename[:-4]
            
            file = open("lyrics/" + str(year) + "/" + filename, "r");
            text = file.read()
            occurrence_names = process(occurrence_names, country, text)

    for word in occurrence_names:
        if word in common_words:
            continue
        
        count = len(occurrence_names[word])
        
        if not word in total_occurrence_count:
            total_occurrence_count[word] = 0

        total_occurrence_count[word] = total_occurrence_count[word] + count

# Make a frequency table
frequency_table = [[] for i in range(0, 25)]

for word in total_occurrence_count:
    avg = int(math.floor(total_occurrence_count[word]/len(years)))
    frequency_table[avg].append(word)

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

