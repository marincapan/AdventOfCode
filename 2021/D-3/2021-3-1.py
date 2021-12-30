import os
path=os.getcwd()
L = {}
for i in range(0,13,1):
    L[i]={0:0,1:0}
counter=0
with open("%s\\2021\\D-3\\2021-3-IN.txt"%(path)) as f:
    for line in f:
        for c in line:
            if c=="0":
                L[counter][0]+=1
            else:
                L[counter][1]+=1
            counter+=1
        counter=0
binary=""
print(L)
for k,v in L.items():
    if L[k][0]>L[k][1]:
        binary+="0"
    else:
        binary+="1"
decimal=0
reverse_decimal=0
reverse_binary=""
counter=12
for bit in binary:
    if bit=="0":
        reverse_binary+="1"
        reverse_decimal+=pow(2,counter)
    elif bit=="1":
        decimal+=pow(2,counter)
        reverse_binary+="0"
    else:
        continue
    counter-=1
print(binary)
print(reverse_binary)
print(decimal)
print(reverse_decimal)
print(decimal*reverse_decimal)