#!/usr/bin/python3.9

from collections import Counter
from bs4 import BeautifulSoup
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('file')

args = parser.parse_args()

with open(args.file, 'r') as fp:
    soup = BeautifulSoup(fp, 'lxml')

def filter_alpha(word: str) -> str:
    return ''.join([c for c in word if c.isalpha()])

names_lower = [el.string.lower() for el in soup.select('p.comment-text>span')]
names_lower_letters_only = map(filter_alpha, names_lower)

print(Counter(names_lower))
print()
print(Counter(names_lower_letters_only))
