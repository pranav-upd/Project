import csv
import sys
l = len(sys.argv)
if l != 3:
    print("Usage: python file.csv file.txt")
    exit(1)
#..
b = 0
#..
csv_file = csv.DictReader(open(sys.argv[1]))
txt_file = open(sys.argv[2])
#..
c = ""
for b in txt_file:
    c = c + b
#..
t = 0
for data in csv_file:
    keydata = data.keys()
    ln = len(keydata)
    ln = ln - 1
    for a in keydata:
        if a != "name":
           d = int(data[a])
           n = c.count(a)
           print(d,n)
           if d == n:
               t = t + 1
           if t == ln:
               print(data["name"])
               exit(0)
        if a == "name":
            t = 0
print("No match")













