import os
import sys

if len(sys.argv) != 3:
	print("Error: 2 cml arguments required: string and directory.")
	sys.exit(1)

string = sys.argv[1]
directory = sys.argv[2]

for root, dirs, files in os.walk(directory):
    for file in files:
        if string in str(file):
            print(os.path.join(root, file))
