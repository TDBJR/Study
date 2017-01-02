import os

man=[]
other=[]

try:
    data=open('c:/text/text.txt')
                                                 
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':',1) 
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)             
                  
        except ValueError:
            print('test error')
    data.close()                 

except IOError:
    print('File not found')
data.close()                                     
print(man)
print(other)