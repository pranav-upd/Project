from cs50 import get_int
#..
h = 0
while h<1 or h>8:
     h = get_int("Height: ")
#..
i = 0
j = 0
k = 0
#..
for j in range(h):
    while k < h-(j+1):
        print(" ",end="")
        k = k + 1
    #...
    while i < j+1:
        print("#",end="")
        i = i + 1
    print("")
    i = 0
    k = 0

