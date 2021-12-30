import os
path=os.getcwd()
L = []
with open("%s\\2021\\D-1\\2021-1-IN.txt"%(path)) as f:
    for line in f:
        L.append(int(line))
measures={}
counter=0
"""part one od day one
for i in range(0,len(L),1):
    if (i==0):
        measures[L[i]]="N/A - no previous measurement"
    else:
        if L[i]<L[i-1]:
            measures[L[i]]="decreased"
        else:
            measures[L[i]]="increased"
            counter+=1
print(counter)
"""
for i in range(0,len(L),1):
    try:
        measures[counter]=L[i]+L[i+1]+L[i+2]
        counter+=1
    except IndexError:
        continue
counter2=0
for k,v in measures.items():
    try:
        if measures[k+1]>measures[k]:
            counter2+=1
    except KeyError:
        continue
print(counter2)