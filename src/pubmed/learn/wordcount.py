import re
from collections import Counter
import csv

f = open('sample2.txt', 'r')

words = f.read().split(" ")
new_words = []
for word in words:
    word = re.sub(r'[.!,:;()\'\"]', '', word)
    word = word.lower()
    new_words.append(word)

wordcount = Counter(new_words)
print(wordcount)

with open('wordcount.csv', mode='w') as csv_file:
    fieldnames = ['word', 'count']
    writer = csv.writer(csv_file)
    writer.writerow(fieldnames)
    for key, value in wordcount.items():
        writer.writerow([key] + [value])

f.close()
csv_file.close()
