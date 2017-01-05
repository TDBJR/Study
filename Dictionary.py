# Dictionary

cleese = {}
palin = dict() # Both of these lines are creating a Dictionary

cleese['Name'] = 'John Cleese'
cleese['Occupations'] = ['actor', 'comedian', 'writer', 'film producer']

palin = {'Name': 'Michael Palin', 'Occupations': ['comedian', 'actor', 'writer', 'tv']}


print(palin['Name']) # You need to use square brackets when calling data from inside a Dictionary 
'Michael Palin'

print(cleese['Occupations'][-1]) # Occupation is a list, you can call the last item on the list with -1, 
'film producer'                  # The second to last with -2, third to last -3 ect 

palin['Birthplace'] = "Broomhill, Sheffield, England"
cleese['Birthplace'] = "Weston-super-Mare, North Somerset, England" # You can continue to add to the 
                                                                    # palin and cleese Dictionary database
                                                                    
# Unlike lists, a Python dictionary does not maintain insertion order, which can result in some unexpected
# behavior. The key point is that the dictionary maintains the associations, not the ordering
# The order of the items in the lists seem to stay, but not the order of the list variables Name,occupations,birthplace
# will appear in a different order. print(cleese['Occupations'][-1]) will alway print 'film producer' in this case.

