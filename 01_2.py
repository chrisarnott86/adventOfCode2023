import re
with open('input1.txt','r') as file:
#with open('input1-test2.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

nums = ['one','two','three','four','five','six','seven','eight','nine','ten']
portwords = {'oneight':'18','twone':'21','threeight':'38','fiveight':'58','sevenine':'79','eightwo':'82','nineight':'98','tenine':'10'}
linetot=0
for line in lines:
    for port, sub in portwords.items():
        line = re.sub(port, sub, line)
    for i,_ in enumerate(line):
        for j,num in enumerate(nums):
            if (num in line[i:i+len(num)]):
                line = re.sub(num, str(j+1), line, count=1)
    temp = re.findall(r'\d+', line)
    temp = ''.join(temp)
    number= int(temp[0]+temp[-1])
    linetot+=number

print(linetot)
