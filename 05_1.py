with open('input5.txt','r') as file:
#with open('input5-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

maps=[]

for line in lines:
    if 'map' in line:
        maps.append.append(0)
    else:
        ops.append(int(line.split()[1]))
