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


def Run(file='c:/'):
# This is opening a txt file and calling both of the above
# methods, then converting it into a readable dictionary 
    name=OpenXL(file)                       
    (name1,dob1)=name.pop(0),name.pop(0)
    info={'Name':name1,'Dob':dob1,'Fastest Times':str(sorted(set([Convert(t)for t in name]))[:3])}
    print(info) # The above : means equals       
                                               
Run('c:/PHF/james2.txt')
Run("c:/PHF/julie2.txt")
Run("c:/PHF/mikey2.txt")
Run("c:/PHF/sarah2.txt")

