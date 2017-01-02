movies = [ "The Holy Grail", 1975, "Terry Jones & Terry Gilliam",
91,["Graham Chapman", ["Michael Palin",
"John Cleese", ["Terry Gilliam", "Eric Idle",
"Terry Jones"]]]]

def List8(self,indent=False,alt=0):
    for each_item in self:
        if isinstance(each_item, list):
            List8(each_item,indent,alt+1)
        elif indent:
            for tab_stop in range(alt):
                print("\t",end='') #<-- end='' adds a single blank space after a print instead 
            print(each_item)       # of the defualt \n that adds a new blank line
        else:                      # \t will add a tab space that is 4 spaces per loop cycle
            print(each_item)

'''below is creating a loop that will cycle the amount of times that are equal 
to the amount of items stored in movies'''   

for each_item in movies:
    # below is asking if any items in the list contain further lists
    if isinstance(each_item, list):
     #below is calling the imported method
        List8(each_item)
    else:
        print(each_item)


