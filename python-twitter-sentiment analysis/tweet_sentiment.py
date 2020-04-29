# -*- coding: utf-8 -*-
import sys
import json
import string


def main():
    senti_file = open(sys.argv[1])
    scores = {}
    for line in senti_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        d = json.loads(line.encode('utf8'))
        if 'text' in d.keys():
            exclude = set(string.punctuation)
            word = ''.join(ch for ch in d['text'].encode('utf8').lower() if ch not in exclude)
            return word


if __name__ == '__main__':
    main()
