from cs50 import get_string
#..
user_input = get_string("Text: ")
#..
l = 0
t = 0
sc = 0
b = 1
w = 0
index = 0
for s in user_input:
    if s != " ":
        if bool(b) == True:
            w = w + 1
        b = 0
        t = ord(s)
        if (t>=65 and t<=90) or (t>=97 and t<=122):
            l = l + 1
        #..
        if (s == ".") or (s == "!") or (s == "?"):
            sc = sc + 1
    if s == " ":
        b = 1
#..
l = l/w
l = l * 100
l = round(l, 2)
sc = sc/w
sc = sc * 100
sc = round(sc, 2)
index = 0.0588 * l - 0.296 * sc - 15.8
index = round(index)
if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")









