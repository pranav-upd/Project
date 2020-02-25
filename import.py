import csv
import sys
import cs50

db = cs50.SQL("sqlite:///students.db")
#..
c = 0
a = 0
num = 0
name = ""
first_name = ""
middle_name = None
last_name = ""
house = ""
birth = ""
#..
l = len(sys.argv)
if l != 2:
    print("Usage: python file.csv")
    exit(1)
#..
csv_file = csv.DictReader(open(sys.argv[1]))
for j in csv_file:
    name = j["name"]
    for i in name:
        if i == " ":
            c = c + 1
    if c == 1:
        for i in name:
            if i == " ":
                a = a + 1
                continue
            if a == 0:
                first_name = first_name + i
            if a == 1:
                last_name = last_name + i
    #..
    if c == 2:
        for i in name:
            if i == " ":
                a = a + 1
                continue
            if a == 0:
                first_name = first_name + i
            if a == 1:
                middle_name = middle_name + i
            if a == 2:
                last_name = last_name + i

    house = j["house"]
    birth = j["birth"]
    num = num + 1
    #..
    db.execute("INSERT INTO students (id, first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?, ?)",
    num, first_name, middle_name, last_name, house, birth)
    #..
    first_name = ""
    middle_name = None
    last_name = ""
    name = ""
    house = ""
    birth = ""
    c = 0
    a = 0
    i = ""





