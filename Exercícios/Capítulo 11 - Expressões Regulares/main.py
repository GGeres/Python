import re

hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    if re.search('ˆX\S*: [0-9.]+', line):
        print(line)
