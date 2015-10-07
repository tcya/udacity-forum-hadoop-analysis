#!/usr/bin/python
import sys

this_id = None
attendance = []

# Loop around the data
# It will be in the format key\tval
# Where key is the post_id, val is the id who posts it
#
# All the ids for a particular post will be summarized to a list "attendance"
# then the key will change and we'll be dealing with the next post

for line in sys.stdin:
    data_mapped = line.split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    post_id, student_id = data_mapped
    student_id = int(student_id.replace('\n', ''))

    if this_id and post_id != this_id:
        print '{0}\t{1}'.format(this_id, attendance)
        this_id = post_id
        attendance = []

    this_id = post_id
    attendance.append(student_id)

if post_id != None:
    print '{0}\t{1}'.format(this_id, attendance)
