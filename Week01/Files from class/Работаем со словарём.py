table = {'Sjored': 4127, 'Jack': 2345, 'Dcab': 5435}

longest_name_length = 0
longest_name = ''

for name, phone in table.items():
    #len(name)
    

    s = 0
    for letter in name:
        s += 1
        #print(letter)
    

    if s > longest_name_length:
        longest_name_length = s 
        longest_name = name
        
print(f'Longest name is {longest_name} and its length is {longest_name_length}')
print(table[longest_name])
    
