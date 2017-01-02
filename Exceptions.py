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
                  
        except ValueError as err:
            print('test error'+str(err))
                        

except IOError as err:
    print('File not found'+str(err))
finally:
    data.close()                                     
try:
    data2=open('c:/text/man.txt','w')
    data3=open('c:/text/other.txt','w')
    print(man,file=data2)
    print(other,file=data3)
    
except IOError as err:
    print('file error'+str(err))
    
finally:
    data2.close()
    data3.close()