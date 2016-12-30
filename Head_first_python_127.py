import os
import sys
man=[]
other=[]
def print_lol(the_list, indent=False, level=0,fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1,fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='',file=fh)
                    print(each_item,file=fh )


with open('c:/text/text.txt') as data:                                                 
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':',1) 
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)             
              
        except ValueError as err:
            print('test error'+err)
                                                             
try:
    data2=open('c:/text/man.txt','w')
    data3=open('c:/text/other.txt','w')
    print_lol(man,file=data2)
    print_lol(other,file=data3)
    
except IOError as err:
    print('file error'+err)
    