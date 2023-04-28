import csv
from loremipsum import get_sentences, get_paragraphs
from uuid import uuid4
from random import choice

# read students.csv file
with open('students.csv', newline='') as students_file:
    students_reader = csv.reader(students_file)
    next(students_reader)  # skip header row
    user_ids = [row[2] for row in students_reader]

# read forums.csv file
with open('forums.csv', newline='') as forums_file:
    forums_reader = csv.reader(forums_file)
    next(forums_reader)  # skip header row
    forums = [row[0] for row in forums_reader]

# create thread list of lists
thread = [['forum_id', 'thread_id', 'title', 'content', 'user_id']]
for forum_id in forums:
    thread_id = uuid4().hex
    title = get_sentences(1)[0]
    content = get_paragraphs(1)[0]
    user_id = choice(user_ids)
    thread.append([forum_id, thread_id, title, content, user_id])

# save thread list to thread.csv file
with open('thread.csv', 'w', newline='') as thread_file:
    thread_writer = csv.writer(thread_file)
    thread_writer.writerows(thread)
