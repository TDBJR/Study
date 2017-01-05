import pickle
from tomodules import fetus

def put_to_store(file_list):
    for each_item in file_list:
        all_athletes = {}
        ath=fetus.Alist.OpenXL(each_item)
        all_athletes[ath.name] = ath
    #print(all_athletes)   #This call to print functions as expected listing all the expected data
    try:
        with open('athletes.pickle','wb') as athf:
            pickle.dump(all_athletes,athf)
    except IOError as ioerr:
        print('File error (put_and_store): ' + str(ioerr))
    #print(all_athletes)    # This only prints the last expected Dictionary entry and it's data
    return(all_athletes)

def get_from_store():
    all_athletes={}
    try:
        with open('athletes.pickle','rb') as athf:
            all_athletes=pickle.load(athf)
    except IOError as ioerr:
        print('File error(get_from_store)' +str(ioerr))

the_files = ['c:/PHF/sarah2.txt', 'c:/PHF/james2.txt', 'c:/PHF/mikey2.txt', 'c:/PHF/julie2.txt']
data = put_to_store(the_files)
#===============================================================================
# print(data)  # this stuff only contains the last Dictionary entry of an expect 4
# for each_athlete in data:
#     print(data[each_athlete].name + ' ' + data[each_athlete].dob) 
#===============================================================================
