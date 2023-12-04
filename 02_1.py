with open('input2.txt','r') as file:
#with open('input2-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

limits = {'red':12,'green':13,'blue':14}

count = 0
for id,line in enumerate(lines):
    line=line.split(': ')[1]
    games = line.split('; ')
    valid=True
    for game in games:
        hands = game.split(', ')
        for hand in hands:
             num=int(hand.split()[0])
             col=hand.split()[1]
             if num>limits[col]:
                 valid=False
    if valid:
        count+=(id+1)
        
print(count)
