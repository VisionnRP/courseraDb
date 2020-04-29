import sys
import json


def main():
    tsags = {}
    for line in open(sys.argv[1]):
        tweet = json.loads(line)
        if "entities" in tweet:
            entities = tweet["entities"]
            curr_tags = entities["hashtags"]
            for tag in curr_tags:
                tag = tag["text"]
                if tag in tsags.keys():
                    tsags[tag] += 1
                else:
                    tsags[tag] = 1


if __name__ == '__main__':
    main()
