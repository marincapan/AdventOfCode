import os
path=os.getcwd()
L = {}
horizontal=0
depth=0
with open("%s\\2021\\D-2\\2021-2-IN.txt"%(path)) as f:
    for line in f:
        L[line.split(" ")[0]]=int(line.split(" ")[1])
        if line.split(" ")[0] == "forward":
            horizontal+=int(line.split(" ")[1])
        elif line.split(" ")[0] == "down":
            depth+=int(line.split(" ")[1])
        else:
            depth-=int(line.split(" ")[1])
print("%d %d %d"%(horizontal,depth,horizontal*depth))