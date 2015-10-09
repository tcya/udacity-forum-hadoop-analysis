#!/usr/bin/python
#Print post_id  post_length  post_type
import sys
import csv

for line in csv.reader(sys.stdin, delimiter='\t'):
    if line[0] == 'id':
        continue
    if len(line) != 19:
        continue
    body = line[4]
    post_type = line[5]
    if post_type == 'question':
        print '{0}\t{1}\t{2}'.format(line[0], len(body), 'Q')
    elif post_type == 'answer':
        print '{0}\t{1}\t{2}'.format(line[7], float(len(body)), 'A')
    else:
        print 'Unrecognized post type. It should be "question" or "answer", but it\'s ', post_type
