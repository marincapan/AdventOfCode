L = []
with open('2020-1-IN.txt') as f:
    for line in f:
        L.append(int(line))
#print(L)
for i in range(0, len(L), 1):
    for j in range(i+1, len(L), 1):
        for k in range(j+1, len(L), 1):
            if ((L[i]+L[j]+L[k])==2020):
                print(L[i]*L[j]*L[k])
                break
        
            
