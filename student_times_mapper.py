#!/usr/bin/python
# Print author_id   time_posted

import sys
import time
import csv

for line in csv.reader(sys.stdin, delimiter='\t'):
    if line[0] == 'id':
        continue
    if len(line) != 19:
        continue
    author_id = line[3]
    hour = line[8].split('.')[0]
    t = time.strptime(hour,'%Y-%m-%d %H:%M:%S')
    print '{0}\t{1}'.format(author_id, t.tm_hour)
    tmp = ''
