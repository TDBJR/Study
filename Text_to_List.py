def One(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'            
    else:
        return(time_string)      #<---------------stops the function and prints the results
    (mins,secs)= time_string.split(splitter)
    return(mins + '.' + secs)

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

clean_james=[]
clean_julie=[]
clean_mikey=[]
clean_sarah=[]

for each_s in james:   # In a for loop each_s becomes the mutible james which is why you have to call it instead of james
    clean_james.append(One(each_s))
for each_s in julie:
    clean_julie.append(One(each_s))
for each_s in mikey:
    clean_mikey.append(One(each_s))
for each_s in sarah:
    clean_sarah.append(One(each_s))

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))