with open('input4.txt','r') as file:
#with open('input4-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

totpoints = 0
cardcounts={i+1:1 for i in range(len(lines))}

for i,line in enumerate(lines):
    line=line.split(': ')[1]
    draw = set(i for i in line.split(' | ')[0].split())
    winners = set(i for i in line.split(' | ')[1].split())

    won = len(draw.intersection(winners))
    if won>0:
       for _ in range(cardcounts[i+1]):
            for j in range(won):
                cardcounts[(i+1)+(j+1)]+=1
    
print(sum(cardcounts.values()))
