#!/usr/bin/python
#Print the tags for every post. Every time only one tag is printed
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
    # Handle multiple-line-entry. A row is complete when it accumulates 19 items separated by \t.
    tmp += line
    row = tmp.split('\t')
    if len(row) == 19:
        tmp = ''
        post_type = remove_quotes(row[5])
        if post_type == 'question':
            tag = remove_quotes(row[2])
            tag = tag.split()
            for t in tag:
                print t
    elif len(row) > 19:
        print 'Reading error in line ', line
        break

