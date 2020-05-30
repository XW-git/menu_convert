'''
convert file 
usage: cvt abc.txt
it generates abc.csv
this first check in just demo read and print file
'''

file1=open("abc.txt", "r")
count = 0;

while True:
    count += 1

    # Get next line from file
    line = file1.readline()

    # if line is empty
    # end of file is reached
    if not line:
        break

    if line=='\n':
        print("Line{}: this is empty line".format(count) )
    else:
        print("Line{}: {}".format(count, line.strip()))

file1.close()