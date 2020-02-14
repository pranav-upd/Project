import csv
import sys
l = len(sys.argv)
if l != 3:
    print("Usage: python file.csv file.txt")
    exit(1)
csv_file = csv.DictReader(open(sys.argv[1]))
for data in csv_file:
    keydata = data.keys()
#..





txt_file = sys.argv[2]



