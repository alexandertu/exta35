import sys
import re

file = open('data/exta35.txt') # open(sys.argv[0])
data = file.read()
lines = data.split('\n')

lines2 = []
for i in range(len(lines)):
    if i % 2 != 0:
        lines2.append(lines[i])

csv = []
for l in lines2:
    l = re.sub('<div>', '', l)
    l = re.sub('</div>', '', l)
    l = re.sub('&nbsp', '', l)
    l = re.sub(',', ';', l)
    l = re.sub('-;', ',', l)
    l = re.sub('\t', ',', l)
    csv.append(l)
