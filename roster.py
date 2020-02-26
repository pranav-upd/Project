import sys
import cs50
#..
db = cs50.SQL("sqlite:///students.db")
l = len(sys.argv)
if l != 2:
    print("Usage: python roster.py house")
    exit(1)
house = sys.argv[1]
student_id = 1
data = {}
middle_name = ""
data = db.execute("SELECT first, middle, last, birth from students WHERE house = ?", house)
for i in data:
    print(i["first"], end=" ")
    if i["middle"] == None:
        print("",end = "")
    else:
        print(i["middle"], end=" ")
    print(i["last"], end=", ")
    print("born",i["birth"])


