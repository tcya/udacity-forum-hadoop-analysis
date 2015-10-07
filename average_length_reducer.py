#!/usr/bin/python
import sys

this_id = None
ans_len = []
q_len = 0

# Loop around the data
# It will be in the format key\tval1\tval2
# Where key is the post_id, val1 is the length of the post, val2 is the type of the post
#
# The length of the question, and the average length of all answers for a particular post will be presented,
# then the key will change and we'll be dealing with the next post

for line in sys.stdin:
    data_mapped = line.split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue
    post_id, length, post_type = data_mapped

    if this_id and post_id != this_id:
        if ans_len:
            avg_ans_len = sum(ans_len)/len(ans_len)
        else:
            avg_ans_len = 0
        print '{0}\t{1}\t{2}'.format(this_id, q_len, avg_ans_len)
        this_id = post_id
        ans_len = []
        q_len = 0

    this_id = post_id
    if post_type == 'Q\n':
        q_len = length
    elif post_type == 'A\n':
        ans_len.append(float(length))
    else:
        print 'Unrecognized post type ', post_type, ' in line: ', line

if post_id != None:
    if ans_len:
        avg_ans_len = sum(ans_len)/len(ans_len)
    else:
        avg_ans_len = 0
    print '{0}\t{1}\t{2}'.format(this_id, q_len, avg_ans_len)
