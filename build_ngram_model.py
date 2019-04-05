# Part 1 - Building NGram Models
#
# Level 1 - may use NLTK Levels 2/3 - may not use NLTK
#
# Write a script called build_ngram_model.py, that takes in an input file and outputs a
# file with the probabilities for each unigram, bigram, and trigram of the input text.
#
# The script should run with the following command:
# ./build_ngram_model.py <input_file> <output_file>
#
# The input file format is 1 sentence per line, with spaces between every word. (The files
# are pre-tokenized).
#
# Add beginning of sentence (<s>) and end of sentence tags (</s>) and make everything
# lowercase.
# For example, if a sentence is:
# Hello , my cat !
# You will count as if the sentence is written:
# <s> hello , my cat ! </s>
#
# The output file should have the following format: (see sample file: dickens_model.txt)
# \data\
# ngram 1: types=<# of unique unigram types> tokens=<total # of unigram tokens>
# ngram 2: types=<# of unique bigram types> tokens=<total # of bigram tokens>
# ngram 3: types=<# of unique trigram types> tokens=<total # of trigram tokens>
#
# \1-grams:
# <list of unigrams>
#
# \2-grams:
# <list of bigrams>
#
# \3-grams:
# <list of trigrams>
#
# The lists should include the following, in order, separated by spaces:
#
# Count of n-gram
# Probability of n-gram (P(wn | wn-1) for bigram and P(wn | wn-2 wn-1) for trigram)
# Log-prob of n-gram (take the log base 10 of the probability above)
# n-gram
#
# Do not use smoothing for this! Only include n-grams that exist in the training text.

import sys
from nltk.util import ngrams
import math


# define i/o:
input_file = sys.argv[1]
output_file = sys.argv[2]

in_lines = open(input_file, encoding='utf-8').readlines()



# [count of ngram] [probability of ngram] [log-prob of n-gram] [ngram itself]
# token = nltk.word_tokenize(text)
# bigrams = ngrams(token,2)
# trigrams = ngrams(token,3)
# fourgrams = ngrams(token,4)
# fivegrams = ngrams(token,5)

def input_cleaning(x):
    # takes a list of sentences, makes everything lowercase and adds <s> at the beginning of sentence
    # and </s> at the end of each sentence
    clean = []
    for i in x:
        i = i.lower()
        i = '<s> ' + i + ' </s>'
        clean.append(i)
    return clean


def get_unigrams(lines, out):
    # \1-grams:
    # 123606 0.035701824517297795 -1.4473095889985277 the
    # count  probability          log(probability)    ngram

    one_grams = []
    for line in lines:
        line_one_grams = ngrams(line.split(), 1)
        for x in line_one_grams:
            one_grams.append(x[0])
    # outputs [('<s>',), ('from',), ('fairest',), ('creatures',), ('we',), ('desire',), ('increase',), (',',), ('that',), ('thereby',)]
    print(one_grams[:10])

    length = len(one_grams)

    to_sort = []
    for x in one_grams:
        count = one_grams.count(x)
        prob = count / length
        logprob = math.log10(prob)
        line_data = (count, prob, logprob, x)
        to_sort.append(line_data)

    sorted_lines = sorted(to_sort, key=lambda tup: tup[0], reverse=True)
    for x in sorted_lines:
        line = str(x[0]) + ' ' + str(x[1]) + ' ' + str(x[2]) + ' ' + x[3]
        out.append(line)

    return out





def get_bigrams(lines, out):
    # \1-grams:
    # 123606 0.035701824517297795 -1.4473095889985277 the
    # count  probability          log(probability)    ngram

    bi_grams = []
    one_grams = []
    for line in lines:
        bi_grams.append(ngrams(line.split(), 2))
    for x in bi_grams:
        print(x)
        one_grams.append(x(0))
    # outputs [('<s>', 'i—first'), ('i—first', 'quarter'), ('quarter', '.'), ('.', '</s>'), ('<s>', 'there'), ('there', 'are'), ('are', 'not'), ('not', 'many'), ('many', 'people—and'), ('people—and', 'as')]
    print(bi_grams[:10])

    length = len(bi_grams)

    to_sort = []
    for x in bi_grams:
        count = bi_grams.count(x)
        prob = count / one_grams.count(x[0])
        logprob = math.log10(prob)
        line_data = (count, prob, logprob, x)
        to_sort.append(line_data)

    sorted_lines = sorted(to_sort, key=lambda tup: tup[0], reverse=True)
    for x in sorted_lines:
        line = str(x[0]) + ' ' + str(x[1]) + ' ' + str(x[2]) + ' ' + x[3]
        out.append(line)

    return out


#def get_trigrams(x):


clean_lines = input_cleaning(in_lines)
out_lines = []

out_lines.append('')
out_lines.append('\\1-grams:')
#out_lines.append(get_unigrams(clean_lines, out_lines))

out_lines.append('')
out_lines.append('\\2-grams:')
out_lines.append(get_bigrams(clean_lines, out_lines))


print(out_lines[:20])


