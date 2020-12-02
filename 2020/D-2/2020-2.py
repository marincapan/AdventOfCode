counter = 0

with open('2020-2-IN.txt') as f:
    for line in f:
        L=line.split(" ")
        l=L[0].split("-")
        min_letter = int(l[0])
        max_letter = int(l[1])
        #print(min_letter)
        #print(max_letter)
        m=L[1].split(":")
        letter = str(m[0])
        #print(letter)
        password = L[2]
        #print(password)
        try:
            if (password[min_letter-1]==letter and password[max_letter-1]!=letter):
                counter+=1
            if (password[min_letter-1]!=letter and password[max_letter-1]==letter):
                counter+=1
        except:
            continue
"""        all_freq = {} 
  
        for i in password: 
            if i in all_freq: 
                all_freq[str(i)] += 1
            else: 
                all_freq[str(i)] = 1
        #print(all_freq[letter])
        try:
            if (all_freq[letter] >= min_letter and all_freq[letter] <= max_letter):
                counter+=1
        except KeyError:
            continue
"""
    
print(counter)
        
