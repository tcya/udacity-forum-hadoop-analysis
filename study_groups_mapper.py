#!/usr/bin/python
# Print post_id   author_id
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
        if remove_quotes(row[0]) == 'id':
            tmp = ''
            continue
        tmp = ''
        author_id = remove_quotes(row[3])
        post_type = remove_quotes(row[5])
        if post_type == 'question':
            post_id =  remove_quotes(row[0])
            print '{0}\t{1}'.format(int(post_id), author_id)
        elif post_type in ['answer', 'comment']:
            post_id = remove_quotes(row[7])
            print '{0}\t{1}'.format(int(post_id), author_id)
        else:
            print 'Unrecognized post type. It should be "question", "answer" or "comment", but it\'s ', post_type
    elif len(row) > 19:
        print 'Reading error in line ', line
        break
