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

#====================Method==Variable====Variable===List=========[List==Comprehension]=================================
clean_sarah= [Convert(symbol) for symbol in sarah] #<-------- You can either sort the list itself
clean_mikey= sorted([Convert(symbol) for symbol in mikey])  # or you can print out the contents 
clean_julie= sorted([Convert(symbol) for symbol in julie])  # sorted while not affecting the list
clean_james= sorted([Convert(symbol) for symbol in james])  # with print(sorted(list_name))
                                                            # see the print command at the bottom
#===========================================Sets===============================================================================
unique_james= sorted(set(clean_james))   # Once Sets are created the contents cannot be altered,   #  unique_james=set(james)
unique_sarah= sorted(set(clean_sarah))   # although the set variable can be set to a new value.  <---unique_james=something new
unique_julie= sorted(set(clean_julie))   # set() is a list that will not take in duplicates.           
unique_mikey= sorted(set(clean_mikey))   # if the imported list contains duplicate strings,variables or numbers.
                                         # only the first item will be added to the set list.
 # sorted must come before set           # if you want to remove duplicate entries in a list you can conver it to a set
#===========================================Removing==Duplicates==From==Lists====================================================================================


# for each_unit in clean_james:
#     if each_unit not in unique_james:    #<---Removing not would leave the list empty
#         unique_james.append(each_unit)   #<---since there is nothing in unique_james
#         
# for each_unit in clean_sarah:
#     if each_unit not in unique_sarah:
#         unique_sarah.append(each_unit)
# 
# for each_unit in clean_julie:
#     if each_unit not in unique_julie:
#         unique_julie.append(each_unit)
#         
# for each_unit in clean_mikey:
#     if each_unit not in unique_mikey:
#         unique_mikey.append(each_unit)
#===============================================================================

#===============================================================================================================================        
print('James:',unique_james[:3])   
print('Sarah:',sorted(unique_sarah)[:3])   # sorted(set(object)[:3]) can be used on the print and return lines too
print('Julie:',unique_julie[:3])
print('Mikey:',unique_mikey[:3])