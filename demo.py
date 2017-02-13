from visual_decoding import visual_decoding
import os
import sys

prfx = sys.argv[1]
n = int(sys.argv[2]) - 1

f_tokens = []
N = 0
while True:
    if os.path.exists('%s%d' % (prfx, N)):
        f_tokens.append(open('%s%d' % (prfx, N), 'r'))
        N += 1
    else:
        break

sentences = []

for lines in zip(*f_tokens):

    sentences.append([])
    for line in lines:
        sentences[-1].append(line.strip())

for t in f_tokens:
    t.close()

sentence = sentences[n]
sentence = [s.split() for s in sentence]

visual_decoding(sent=sentence)