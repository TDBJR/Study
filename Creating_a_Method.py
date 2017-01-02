
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
# def Detwin(womb):
#     fetus=[]
#     for twin in womb:           
#         if twin not in fetus:    
#             fetus.append(twin)
#     return(fetus)#<--------------Always keep return out of the loop
#===============================================================================
    


def Detwin(womb):     # this is a list comprehention of the above loop
    fetus = []
    [fetus.append(twin) for twin in womb if twin not in fetus]
    return fetus

#This stuff is fine
#===============================================================================
james=OpenXL('c:/PHF/james.txt')  # (File contents) 2-34,3:21,2.34,2.45,3.01,2:01,2:01,3:10,2-22

clean_james=sorted([Convert(time) for time in james])

unique_james=Detwin(clean_james)
print(unique_james)
#===============================================================================
# for each_unit in clean_james:
#     if each_unit not in unique_james:    #<---Trying to turn this into a method
#         unique_james.append(each_unit)   
# print(unique_james)        
#===============================================================================
