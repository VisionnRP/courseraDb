import sys
import json
import re


def functionFor(formatted_text, defaultObject):
    funcVariable = defaultObject
    for word in formatted_text:
        if word in defaultObject and word != '':
            funcVariable[word] += 1
        elif word != '':
            defaultObject[word] = 1


def main():
    all_words_count = 0
    defaultObject = {}
    for line in open(sys.argv[1]):
        if "text" in json.loads(line):
            json.loads(line)['text'].encode('ascii', 'replace')
            formatted_text = re.split(r"[\s.,?:!\n]+", json.loads(line)["text"].rstrip("\n"))

            all_words_count += len(formatted_text)

            functionFor(formatted_text, defaultObject)


if __name__ == '__main__':
    main()
