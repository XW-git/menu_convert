'''
convert file 
usage: cvt abc.txt
it generates abc.csv
this first check in just demo read and print file
'''

import sys

def check_cmdline():
  # This method ensures a valid file was provided to the invoked script ##
  if (len(sys.argv) < 2):                #check command line arguments
    print ("Correct Usage:")
    print (sys.argv[0] + " file")
    sys.exit(0)
    
# price is like "12.34"    
def is_price( str ):
    t = str.replace(".", "")
    return t.isdigit()

    
# main program

check_cmdline()

file=open(sys.argv[1], "r")

gen_file=sys.argv[1]+".txt"
file_out=open(gen_file, "w")

count = 0;

i = 0;
title=""

while True:
    # Get next line from file
    line = file.readline()
    line = line.strip()

    # if line is empty, end of file is reached
    if not line:
        break

    
    if line=='\n':
        i = 0
        # reset parameters 
        dish_name = ""
        price = ""            
        description = ""
    else:
        if title=="":
            title=line 
            file_out.write(title + "\n\n\n")
            i = 0
            dish_name = ""
            price = ""            
            description = ""        
        elif dish_name == "" :

            x = line.find("(")
            if x!= -1:
                dish_name= line[0:x-1]
                description=line[x:len(line)]
            else:
                dish_name= line

        else: 
            description += " " + line
            #description=description.strip()
            # check price
            # get the last word
            list = description.split()
            last = list[-1]            # check the last word 
                       
            if( is_price(last)==True ):
                price = last
                description=description.replace(last,"")

    if( price != "" ):
        price=price.strip()
        file_out.write(dish_name + "\t" + price + "\n")
        file_out.write(description + "\n")
        # a empty line indicates new item starts
        file_out.write("\n")        
        # reset parameters 
        dish_name = ""
        price = ""            
        description = ""

   

file.close()
file_out.close()

#show file
file=open(gen_file, "r")
while True:
    line = file.readline()

    # if line is empty, end of file is reached
    if not line:
        break
    
    print(line)

file.close()
