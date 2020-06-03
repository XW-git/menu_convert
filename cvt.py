'''
convert files output in tmp/ folder 
usage: cvt file 
it generates file  to tmp\.
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

tt_ds = False
def get_title_part(line):
    global title
    global title_done
    global tt_ds
    if line=="\n":
        if title=="":
           return
        else:
        #reached title end
            if tt_ds == True:
                file_out.write("</tt_ds>")
            file_out.write("\n\n")
            title_done=True
            return
               
    else:
        if title=="":
            title=line 
            file_out.write("<tt>"+title.strip()+"</tt>" + "\n")
            return  
        else:
            if tt_ds==False:
                tt_ds = True
                file_out.write("<tt_ds>"+line.strip())
            else:
                file_out.write(" "+line.strip())
        
def get_dish_items(line):
    global dish_name
    global description
    global price
    
    line = line.strip()      #strip will remove "\n"
    if dish_name == "" :
        dish_name= line
        x = line.find("(")
        if x!= -1:
            dish_name= line[0:x-1]
            description=line[x:len(line)]

    else: 
        description += " " + line
    
    return            
 
def  check_price_in(str):
    global price
    str=str.strip()
    list = str.split()
    last = list[-1]            # check the last word 
                           
    if( is_price(last)==True ):
        price = last
        str=str.replace(last,"")
    return  str      

def check_items_end():
    global dish_name
    global description
    global price

    if price =="":
        dish_name = check_price_in( dish_name )
    if price =="":
        description = check_price_in( description )    
        
    return

    
# main program

check_cmdline()

file=open(sys.argv[1], "r")

list=sys.argv[1].split("\\")
gen_file=list[-1]
gen_file="tmp\\"+gen_file
print(gen_file)
file_out=open(gen_file, "w")

count = 0;

title=""
title_done= False

dish_name = ""
price = ""            
description = ""

while True:

    # Get next line from file
    line = file.readline()
    #line = line.strip()      strip will remove "/n"

    # if line is empty, end of file is reached
    if not line:
        break

    if title_done == False:
        get_title_part(line)
    else:
        get_dish_items(line)
        check_items_end()           
        if( price != "" ):
            price=price.strip()
            file_out.write(dish_name + "<pr>" + price + "</pr>"  + "\n")
            if description != "":
                file_out.write( "<ds>" + description + "</ds>"  + "\n")
            # a empty line indicates new item starts
            file_out.write("\n")        
            # reset parameters 
            dish_name = ""
            price = ""            
            description = ""


file.close()
file_out.close()

