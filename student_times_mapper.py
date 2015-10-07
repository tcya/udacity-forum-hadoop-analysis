#!/usr/bin/python
# Print author_id   time_posted

import sys
import time

tmp = ''
for line in sys.stdin:
    line = line.replace('"','')
    if line.split('\t')[0] == 'id':
        continue
    # Handle multiple-line-entry. A row is complete when it accumulates 19 items separated by \t.
    tmp += line
    row = tmp.split('\t')
    if len(row) == 19:
        author_id = row[3]
        hour = row[8].split('.')[0]
        t = time.strptime(hour,'%Y-%m-%d %H:%M:%S')
        print '{0}\t{1}'.format(author_id, t.tm_hour)
        tmp = ''
    elif len(row) > 19:
        print 'Reading error in line ', line
        break
