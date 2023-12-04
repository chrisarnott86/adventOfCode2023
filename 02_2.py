with open('input2.txt','r') as file:
#with open('input2-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

count = 0
powersum = 0
for id,line in enumerate(lines):
    line=line.split(': ')[1]
    games = line.split('; ')
    limits = {'red':0,'green':0,'blue':0}
    for game in games:
        hands = game.split(', ')
        for hand in hands:
             num=int(hand.split()[0])
             col=hand.split()[1]
             if num>limits[col]:
                limits[col]=num
    powersum += limits['red']*limits['blue']*limits['green']

print(powersum)
