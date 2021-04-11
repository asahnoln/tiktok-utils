#!/usr/bin/python3.9

from collections import Counter
from bs4 import BeautifulSoup
from argparse import ArgumentParser
from data.synonyms import construct_with_synonyms, replace_with_synonym


def filter_alpha(text: str) -> str:
    '''Filter out nonalpha characters from string
    '''
    return ''.join([c for c in text if c.isalpha()])


parser = ArgumentParser()
parser.add_argument('file')

args = parser.parse_args()

with open(args.file, 'r') as fp:
    soup = BeautifulSoup(fp, 'lxml')

names_lower = [el.string.lower() for el in soup.select('p.comment-text>span')]
names_lower_letters_only = [filter_alpha(x) for x in names_lower]
names_filtered_synonyms = [replace_with_synonym(x) for x in names_lower_letters_only]

print(Counter(names_filtered_synonyms))
print()

print(construct_with_synonyms(names_lower_letters_only))
