import re
with open('input1.txt','r') as file:
#with open('input1-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

linetot=0
for line in lines:
    temp = re.findall(r'\d+', line)
    temp = ''.join(temp)
    number= int(temp[0]+temp[-1])
    linetot+=number

print(linetot)
