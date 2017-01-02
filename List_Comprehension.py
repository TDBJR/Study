def One(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'            
    else:
        return(time_string)      #<---------------stops the function and prints the results
    (mins,secs)= time_string.split(splitter)
    return(mins + '.' + secs)
#==================Module=Above=for=example=explanation======================================
with open('c:/PHF/james.txt') as jaf:
    data = jaf.readline()
    james = data.strip().split(",")
with open('c:/PHF/julie.txt') as juf:
    data = juf.readline()
    julie = data.strip().split(',')
with open('c:/PHF/mikey.txt') as mif:
    data = mif.readline()
    mikey = data.strip().split(',')
with open('c:/PHF/sarah.txt') as saf:
    data = saf.readline()
    sarah = data.strip().split(',')
#==============================================================================                                       
         #List Comprehension             This is the area you would
#clean_james=[One(t) for t in james]    # normally declare the list 
#clean_julie=[One(t) for t in julie]    # variables. They now declare
#clean_mikey=[One(t) for t in mikey]    # and state their contents.
#clean_sarah=[One(t) for t in sarah]    # something the area below
                                       # normally handles when not 
                                       # using list comprehention.
#==================================================================================
# clean_james=[]                        
# clean_julie=[]                                     
# clean_mikey=[]                                     
# clean_sarah=[]                                     
#
#  for t in james:   
#      clean_james.append(One(t))   # List comprehention makes this block unnescessary
#  for t in julie:                  # You basically incase the for loop in sqaure brackets  
#      clean_julie.append(One(t))   # and place the final action before the first for statment
#  for t in mikey:                  # clean_mikey=[One(t) for t in mikey] 
#      clean_mikey.append(One(t))   # becomes for t in mikey:
#  for t in sarah:                  #                      One(t)
#      clean_sarah.append(One(t))   #                      clean_mikey.append(t)
#======================================================================================
                # Sorted List Comprehension
clean_sarah= sorted([One(t) for t in sarah])  # You can either sort the list itself
clean_mikey= sorted([One(t) for t in mikey])  # or you can print out the contents 
clean_julie= sorted([One(t) for t in julie])  # sorted while not affecting the list
clean_james= sorted([One(t) for t in james])  # shown below
#====================================================================================
#print(sorted(clean_james))
#print(sorted(clean_julie))     # This is how you would sort the printed contents
#print(sorted(clean_mikey))     # while leaving the list unaffected
#print(sorted(clean_sarah))
#=====================================================================================
print(clean_james[:3])   # adding [:3] means list items from 0 to 3
print(clean_sarah[:3])   # [:1:4] would be items from 1 to 4
print(clean_julie[:3])
print(clean_mikey[:3])
