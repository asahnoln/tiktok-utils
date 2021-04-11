#!/usr/bin/python3.9

from collections import Counter
from bs4 import BeautifulSoup
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('file')

args = parser.parse_args()

with open(args.file, 'r') as fp:
    soup = BeautifulSoup(fp, 'lxml')

namesLower = [el.string.lower() for el in soup.select('p.comment-text>span')]
namesLowerLettersOnly = [''.join([c for c in x if c.isalpha()]) for x in namesLower]

print(Counter(namesLower))
print()
print(Counter(namesLowerLettersOnly))
