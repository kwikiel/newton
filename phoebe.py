import csv
from collections import Counter

#https://projecteuler.net/project/resources/p059_cipher.txt
#To jest ten plik
with open('dane.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)


print your_list[0]
pierwsza =  your_list[0][0::3]
print "------------"
print your_list

print Counter(pierwsza).most_common()
