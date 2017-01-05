def OpenXL(data):
    try:
# this is opening a txt and splitting it at , 
        with open(data) as txt:
            read = txt.readline()              #.strip() is removing the \n that are placed by defualt
            splitter = read.strip().split(",") #.split() is turning a string into list items at every , with splitter as the list name 
            (name1,dob1)=splitter.pop(0),splitter.pop(0)
            info={'Name':name1,'Dob':dob1,'Fastest Times':str(sorted(set([Convert(t)for t in splitter]))[:3])}
            print(info)      
    except IOError as err:                
        print('file error'+err)

def Convert(time_string):
    # this is converting the - and : characters to .
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'            
    else:                                     # return is a way to tell the method that you want to store the reult.
        return(time_string)      #<-----------# return stops the program 'block' and lets it know what the desired outcome is
    (mins,secs)= time_string.split(splitter)  # In this case you are letting it know that when the method is called, you want
    return(mins + '.' + secs)                 # the new altered data with splitter set to the defined characters.
# Now with the newly returned data with splitter = ':' and '-' you can give the command to split at splitter
# Then update it to return mins, the data on the left side of the split and secs, the data on the right side of the split 
# with '.' between them as the final reult of the method

OpenXL('c:/PHF/james2.txt')
#testing the methods