import re
with open('input6.txt','r') as file:
#with open('input6-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]


races=[]
temp = re.findall(r'\d+',lines[0].split(':')[1].strip())
time = int(''.join(temp))
temp = re.findall(r'\d+',lines[1].split(':')[1].strip())
record = int(''.join(temp))

wincount = 0
for press in range(time):
    distance = press*(time-press)
    if (distance>record):
        wincount+=1
        
print(wincount)
    
