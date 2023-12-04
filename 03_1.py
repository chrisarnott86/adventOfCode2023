with open('input3.txt','r') as file:
#with open('input3-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

symbols={'*', '%', '/', '$', '&', '#', '-', '@', '+', '='}
nums={'0','1','2','3','4','5','6','7','8','9'}
engine=[]
for line in lines:
    engine.append([char for char in line])

def checkAdjacent(a,b,schematic):
    valid=False
    #need to check up, down, left, right
    loops=0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            try:
                temp=schematic[a+x][b+y]
                if temp in symbols:
                    valid=True
            except:
                pass
    return valid

allsum=0
i=0
while i<len(engine):
    j=0
    while j<len(engine[0]):
        if engine[i][j] not in nums:
            j+=1
            continue
        else:
            numstart=j
            inNum=True
            k=1
            while inNum:
                try:
                    if engine[i][j+k] in nums:
                       k+=1
                    else:
                       inNum=False
                except:
                    inNum=False
                    pass
            
            valid=False
            mynum=''
            for l in range(k):
                mynum+=str(engine[i][j+l])
            for l in range(k):
                if checkAdjacent(i,j+l,engine):
                   valid=True
                   break
            j+=k
            if valid:
                allsum+=int(mynum)
    i+=1
            
print(allsum)
