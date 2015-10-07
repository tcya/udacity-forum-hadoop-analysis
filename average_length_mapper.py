#!/usr/bin/python
#Print post_id  post_length  post_type
import sys

def remove_quotes(string):
    if len(string) != 0:
        if string[0] == '"':
            string = string[1:]
        if string[-1] == '"':
            string = string[:-1]
    string = string.replace('""', '"')
    return string

tmp = ''
for line in sys.stdin:
    if line.split('\t')[0] == '"id"':
        continue
    # Handle multiple-line-entry. A row is complete when it accumulates 19 items separated by \t.
    tmp += line
    row = tmp.split('\t')
    if len(row) == 19:
        tmp = ''
        body = remove_quotes(row[4])
        post_type = remove_quotes(row[5])
        if post_type == 'question':
            print '{0}\t{1}\t{2}'.format(row[0], len(body), 'Q')
        elif post_type == 'answer':
            print '{0}\t{1}\t{2}'.format(row[7], float(len(body)), 'A')
        else:
            print 'Unrecognized post type. It should be "question" or "answer", but it\'s ', post_type
    elif len(row) > 19:
        print 'Reading error in line ', line
        break
