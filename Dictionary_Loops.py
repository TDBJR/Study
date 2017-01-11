#This shit is clever  since the loop only sees the the name and not the value printing a dict in a loop will only list the names
# so if you want it to list the value instead you type the name of the dict and the first variable of the for loop  inside square brakets
# the_links[keys]  since keys is going to be the name it really means   the_list['a'] and cylcles through all the names thus printing 
#all the values

the_links={'a':'10','b':'20','c':'30','d':'40','e':'50'}

for key in the_links:
    #print(key) 
    print(the_links[key])            
    # print(the_links)
    
