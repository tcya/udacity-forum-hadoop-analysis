#!/usr/bin/python
import sys

hour_count = {}
this_id = None

# Loop around the data
# It will be in the format key\tval
# Where key is the author's id, val is the hour the post posted
#
# The most active hour(s) for a particular author will be presented,
# then the key will change and we'll be dealing with the next author

for line in sys.stdin:
    data_mapped = line.split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    author_id, hour = data_mapped

    if this_id and author_id != this_id:
        max_post = hour_count[ max(hour_count.iterkeys(), key=(lambda key: hour_count[key])) ]
        hours = [k for k,v in hour_count.items() if v == max_post]
        for h in hours:
            print '{0}\t{1}'.format(this_id, h)
        this_id = author_id
        hour_count = {}

    this_id = author_id
    try:
        hour_count[hour] += 1
    except KeyError:
        hour_count[hour] = 1

if author_id != None:
    max_post = hour_count[ max(hour_count.iterkeys(), key=(lambda key: hour_count[key])) ]
    hours = [k for k,v in hour_count.items() if v == max_post]
    for h in hours:
        print '{0}\t{1}'.format(author_id, h)
