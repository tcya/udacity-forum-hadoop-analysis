#!/usr/bin/python
import sys

this_tag = None
top_tags = [(0, '')] * 10
tag_count = 0

# Loop around the data
# It will be in the format key
# Where key is a tag of a post
#
# The number of appearance for a particular tag will be counted
# then the key will change and we'll be dealing with the next tag

for line in sys.stdin:
    tag = line.replace('\n', '')

    if this_tag and tag != this_tag:
        if tag_count > top_tags[0][0]:
            top_tags[0] = (tag_count, this_tag)
            top_tags.sort()
        tag_count = 0

    this_tag = tag
    tag_count += 1

if tag != None:
    if tag_count > top_tags[0][0]:
        top_tags[0] = (tag_count, tag)
        top_tags.sort()
top_tags.reverse()
for t in top_tags:
    print '{0}\t{1}'.format(t[1], t[0])
