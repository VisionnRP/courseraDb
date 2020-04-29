# -*- coding: utf-8 -*-
import sys
import json
import string


def construct_dict(sentiment_score_file):
    file = open(sentiment_score_file)

    scores = {}

    for line in file:
        term, score = line.split("\t")

        scores[term] = int(score)
    return scores


def norm_word(word):
    exclude = set(string.punctuation)

    word = ''.join(ch for ch in word.lower() if ch not in exclude)
    return word


def get_senti(senti_dict, line):
    score = 0
    nwords = []
    for word in line.split(' '):
        if word in dict:

            score += senti_dict[word]
        else:
            nwords.append(word)

    return score, nwords


def main():
    dict = construct_dict(sys.argv[1])
    file = open(sys.argv[2])
    for line in file:
        d = json.loads(line.encode('utf8'))
        if 'text' in d.keys():
            score = 0
            nwords = []
            for word in line.split(' '):
                if word in dict:
                    score += dict[word]
                else:
                    nwords.append(word)
            return score, nwords


if __name__ == '__main__':
    main()
