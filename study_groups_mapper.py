#!/usr/bin/python
# Print post_id   author_id
import sys
import csv

for line in csv.reader(sys.stdin, delimiter='\t'):
    if line[0] == 'id':
        continue
    if len(line) != 19:
        continue
    author_id = line[3]
    post_type = line[5]
    if post_type == 'question':
        post_id =  line[0]
        print '{0}\t{1}'.format(int(post_id), author_id)
    elif post_type in ['answer', 'comment']:
        post_id = line[7]
        print '{0}\t{1}'.format(int(post_id), author_id)
    else:
        print 'Unrecognized post type. It should be "question", "answer" or "comment", but it\'s ', post_type
