from collections import Counter
from bs4 import BeautifulSoup

with open('/home/stalin/Документы/tiktok.html', 'r') as fp:
    soup = BeautifulSoup(fp, 'lxml')

namesLower = [el.string.lower() for el in soup.select('p.comment-text>span')]
namesLowerLettersOnly = [''.join([c for c in x if c.isalpha()]) for x in namesLower]

print(Counter(namesLower))
print()
print(Counter(namesLowerLettersOnly))
