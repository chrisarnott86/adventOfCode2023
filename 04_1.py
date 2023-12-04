with open('input4.txt','r') as file:
#with open('input4-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

totpoints = 0
for line in lines:
    line=line.split(': ')[1]
    draw = set(i for i in line.split(' | ')[0].split())
    winners = set(i for i in line.split(' | ')[1].split())

    won = len(draw.intersection(winners))
    if won>0:
        totpoints+=2**(won-1)
    
print(totpoints)
