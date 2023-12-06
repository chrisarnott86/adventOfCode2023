with open('input6.txt','r') as file:
#with open('input6-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]


races=[]
times = lines[0].split(':')[1].split()
distances = lines[1].split(':')[1].split()

for i,_ in enumerate(times):
    races.append({'time':int(times[i]),'record':int(distances[i])})


countmult = 1
for i,race in enumerate(races):
    wincount = 0
    for press in range(race['time']):
        distance = press*(race['time']-press)
        if (distance>race['record']):
            wincount+=1
    countmult *= wincount
    
print(countmult)
