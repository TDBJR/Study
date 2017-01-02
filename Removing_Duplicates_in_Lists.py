def Convert(time_string):
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

#====================Method==Variable====Variable===List=========[List==Comprehension]=================================
clean_sarah= sorted([Convert(symbol) for symbol in sarah])  # You can either sort the list itself
clean_mikey= sorted([Convert(symbol) for symbol in mikey])  # or you can print out the contents 
clean_julie= sorted([Convert(symbol) for symbol in julie])  # sorted while not affecting the list
clean_james= sorted([Convert(symbol) for symbol in james])  # with print(sorted(list_name))
#====================Method==Variable====Variable===List=========[List==Comprehension]=================================

unique_james=[]
unique_sarah=[]
unique_julie=[]
unique_mikey=[]
#===========================================Removing==Duplicates==From==Lists====================================================================================
for each_unit in clean_james:
    if each_unit not in unique_james:    #<---Removing not would leave the list empty
        unique_james.append(each_unit)   #<---since there is nothing in unique_james
        
for each_unit in clean_sarah:
    if each_unit not in unique_sarah:
        unique_sarah.append(each_unit)

for each_unit in clean_julie:
    if each_unit not in unique_julie:
        unique_julie.append(each_unit)
        
for each_unit in clean_mikey:
    if each_unit not in unique_mikey:
        unique_mikey.append(each_unit)
#===============================================================================================================================        
print('James:',unique_james[:3])   # adding [:3] means list items from 0 to 3
print('Sarah:',unique_sarah[:3])   # [:1:4] would be items from 1 to 4
print('Julie:',unique_julie[:3])
print('Mikey:',unique_mikey[:3])