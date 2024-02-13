import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search(r'ˆX\S*: [0-9.]+', line):
        print(line)
