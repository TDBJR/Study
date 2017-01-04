
def OpenXL(data):
    try:
# this is opening a txt and splitting it at , 
        with open(data) as txt:
            read = txt.readline()
            splitter = read.strip().split(",")
            return(splitter)
    except IOError as err:
        print('file error'+err)


def Convert(time_string):
    # this is converting the - and : characters to .
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'            
    else:
        return(time_string)      
    (mins,secs)= time_string.split(splitter)
    return(mins + '.' + secs)

#===============================================================================
# import sys
# def Run(file=sys.stdout):
#     name=OpenXL(file)                       # just testing if i could call methods in methods (works)
#     (a,b)=name.pop(0),name.pop(0)           # This replaces everything below and makes the process user friendly
#     print(a + "'s fastest times are: " +str(sorted(set([Convert(t) for t in name]))[0:3]))
# Run('c:/PHF/test.txt')
#===============================================================================

james=OpenXL('c:/PHF/james2.txt')  
julie=OpenXL("c:/PHF/julie2.txt")
mikey=OpenXL("c:/PHF/mikey2.txt")
sarah=OpenXL("c:/PHF/sarah2.txt")

(julie_name, julie_dob) = julie.pop(0), julie.pop(0)  # .pop(0) Will remove the first item from a list and 'populate' the variable
(mikey_name, mikey_dob) = mikey.pop(0), mikey.pop(0)  # you asign to it with the removed variable.
(james_name, james_dob) = james.pop(0), james.pop(0)
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)

print(james_name + "'s fastest times are: " +str(sorted(set([Convert(t) for t in james]))[0:3])) # Have to add str() to
print(julie_name + "'s fastest times are: " +str(sorted(set([Convert(t) for t in julie]))[0:3])) # make the numbers into 
print(mikey_name + "'s fastest times are: " +str(sorted(set([Convert(t) for t in mikey]))[0:3])) # a string or it will think
print(sarah_name + "'s fastest times are: " +str(sorted(set([Convert(t) for t in sarah]))[0:3])) # it is a math problem
