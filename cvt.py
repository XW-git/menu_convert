'''
convert file 
usage: cvt abc.txt
it generates abc.csv
this first check in just demo read and print file
'''

import sys

def check_file_provided():
  # This method ensures a valid file was provided to the invoked script ##
  if (len(sys.argv) < 2):                #check command line arguments
    print ""
    print "Error - No file was provided"
    print ""
    print "Correct Usage:"
    print "sys.argv[0] file_to_convert"
    print ""
    sys.exit(0)
  if not os.path.isfile(sys.argv[1]):
    print ""
    print "Error - The file provided does not exist"
    print ""
    sys.exit(0)

file=open(sys.argv[1], "r")
count = 0;

while True:
    count += 1

    # Get next line from file
    line = file.readline()

    # if line is empty, end of file is reached
    if not line:
        break

    if line=='\n':
        print("Line{}: this is empty line".format(count) )
    else:
        print("Line{}: {}".format(count, line.strip()))

file.close()