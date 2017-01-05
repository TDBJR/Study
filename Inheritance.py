class Athletelist(list): #<----When creating a class you only need : unless you want to inherit another classes 
    def __init__(self, a_name, a_dob=None, a_times=[]): # atributes then you would add (class name):
        self.name=a_name  # class attributes need to have self. infront of them                            
        self.dob=a_dob
        self.extend(a_times) # the list will become the time data so you just need to extend it
    #all def methods in line with the init will be a part of the class others will not
    def top3(self):
        return(sorted(set([Convert(t) for t in self]))[0:3])
     
    def add_time(self,time_value): # .append() is how you add a single item to a list
        self.append(time_value)
         
    def add_times(self,list_of_times): # even though this will be a list you do not need to set it to =[]
        self.extend(list_of_times) # .extend() is how you add multiple items to a list at once

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
 
def OpenXL(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            splitter = data.strip().split(',')
            return(Athletelist(splitter.pop(0), splitter.pop(0), splitter))#<- This line is calling the class creation Athlete()
    except IOError as ioerr:                          # and filling the class atributes with the pop() function
        print('File error: ' + str(ioerr))            # removing the first word in splitter and adding it to the 
        return(None)                                  # Class. So the first pop(0) will ne the name since a_name is the first
                                                      # argument in Athlete(self, a_name, a_dob=None, a_times=[]) and the second
                                                      # pop(0) will be the dob. after those are removed and added the rest of the
james = OpenXL('c:/PHF/james2.txt')                   # splitter data is added to the final argument a_times=[] which is a list

#print(sorted(set([Convert(t) for t in james.times]))[0:3]) #Alternative convert/sort
print(james.name+',','Born',james.dob+',','Fastest Times:',james.top3()) # Remember to give methods () when calling them james.top3()

vera = Athletelist('Vera Vi')
print(vera.name)
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['2.22', '1-21','2:22'])
print(vera.top3()) 