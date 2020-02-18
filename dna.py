import csv
import sys
import os
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
for y in txt_file:
    f = y
b = len(f)
AGATC = 0
TTTTTTCT = 0
AATG = 0
TCTAG = 0
GATA = 0
TATC = 0
GAAA = 0
TCTG = 0
c = ""
g = 0
h = 0
i = ""
j = 0
k = 0
while h < b:
    h = h + 1
    j = j + 1
    c = f[g:h]
    while c == "AGATC":
        g = h
        h = h + 5
        c = f[g:h]
        k = k + 1
    if k>AGATC:
        AGATC = k
    if j == 5:
        g = g + 1
        h = g
        j = 0
        c = ""
    k = 0
#..
h = 0
g = 0
j = 0
k = 0
c = ""
#..
while h < b:
    h = h + 1
    j = j + 1
    c = f[g:h]
    while c == "TTTTTTCT":
        g = h
        h = h + 8
        c = f[g:h]
        k = k + 1
    if k>TTTTTTCT:
        TTTTTTCT = k
    if j == 8:
        g = g + 1
        h = g
        j = 0
        c = ""
    k = 0
#..
h = 0
g = 0
j = 0
k = 0
c = ""
#..
while h < b:
    h = h + 1
    j = j + 1
    c = f[g:h]
    while c == "AATG":
        g = h
        h = h + 4
        c = f[g:h]
        k = k + 1
    if k>AATG:
        AATG = k
    if j == 4:
        g = g + 1
        h = g
        j = 0
        c = ""
    k = 0
#..
h = 0
g = 0
j = 0
k = 0
c = ""
#..
while h < b:
    h = h + 1
    j = j + 1
    c = f[g:h]
    while c == "TCTAG":
        g = h
        h = h + 5
        c = f[g:h]
        k = k + 1
    if k>TCTAG:
        TCTAG = k
    if j == 5:
        g = g + 1
        h = g
        j = 0
        c = ""
    k = 0
#..
h = 0
g = 0
j = 0
k = 0
c = ""
#..
while h < b:
    h = h + 1
    j = j + 1
    c = f[g:h]
    while c == "GATA":
        g = h
        h = h + 4
        c = f[g:h]
        k = k + 1
    if k>GATA:
        GATA = k
    if j == 4:
        g = g + 1
        h = g
        j = 0
        c = ""
    k = 0
#..
h = 0
g = 0
j = 0
k = 0
c = ""
#..
while h < b:
    h = h + 1
    j = j + 1
    c = f[g:h]
    while c == "TATC":
        g = h
        h = h + 4
        c = f[g:h]
        k = k + 1
    if k>TATC:
        TATC = k
    if j == 4:
        g = g + 1
        h = g
        j = 0
        c = ""
    k = 0
#..
h = 0
g = 0
j = 0
k = 0
c = ""
#..
if c == "GAAA" :
    GAAA = GAAA + 1
    g = g + len(c)
    h = g
    j = 0
    c = ""
#..
h = 0
g = 0
j = 0
k = 0
c = ""
#..
while h < b:
    h = h + 1
    j = j + 1
    c = f[g:h]
    while c == "GAAA":
        g = h
        h = h + 4
        c = f[g:h]
        k = k + 1
    if k>GAAA:
        GAAA = k
    if j == 4:
        g = g + 1
        h = g
        j = 0
        c = ""
    k = 0
#..
h = 0
g = 0
j = 0
k = 0
c = ""
#..
while h < b:
    h = h + 1
    j = j + 1
    c = f[g:h]
    while c == "TCTG":
        g = h
        h = h + 4
        c = f[g:h]
        k = k + 1
    if k>TCTG:
        TCTG = k
    if j == 4:
        g = g + 1
        h = g
        j = 0
        c = ""
    k = 0
h = 0
g = 0
j = 0
k = 0
c = ""
ln = 0

#..
for i in csv_file:
    ln = len(i.keys())
    ln = ln - 1
    #..
    if ln == 8:
       if int(i["AGATC"]) == AGATC:
           j = j + 1
       if int(i["TTTTTTCT"]) == TTTTTTCT:
           j = j + 1
       if int(i["AATG"]) == AATG:
           j = j + 1
       if int(i["TCTAG"]) == TCTAG:
           j = j + 1
       if int(i["GATA"]) == GATA:
           j = j + 1
       if int(i["TATC"]) == TATC:
           j = j + 1
       if int(i["GAAA"]) == GAAA:
           j = j + 1
       if int(i["TCTG"]) == TCTG:
           j = j + 1
       if j == ln:
           print(i["name"])
           exit(0)
       j = 0
    if ln == 3:
       if int(i["AGATC"]) == AGATC:
            j = j + 1
       if int(i["AATG"]) == AATG:
            j = j + 1
       if int(i["TATC"]) == TATC:
            j = j + 1
       if j == ln:
            print(i["name"])
            exit(0)
       j = 0
print("No match")       














