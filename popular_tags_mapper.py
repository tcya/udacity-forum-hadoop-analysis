#!/usr/bin/python
#Print the tags for every post. Every time only one tag is printed
import sys
import csv

for line in csv.reader(sys.stdin, delimiter='\t'):
    if line[0] == 'id':
        continue
    if len(line) != 19:
        continue
    post_type = line[5]
    if post_type == 'question':
        tag = line[2]
        tag = tag.split()
        for t in tag:
            print t
