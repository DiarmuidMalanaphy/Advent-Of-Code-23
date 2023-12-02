file1 = open('input.txt', 'r')
lines = file1.readlines()
sum = 0
numberDict = ["one",9]
letterList = [['one','two','six'],
              ['four','five','nine'],
              ['three','seven','eight']]

letterDict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
for line in lines:
    firstNumber = ''
    lastNumber = ''
    
    for i in range(0, len(line)):
        char = line[i]
        if char.isnumeric():
            if  firstNumber == '':
                firstNumber = char
                lastNumber = char
            else:
                lastNumber = char
        else:
            dist = len(line)-i
            
            for j in range(3, 6):

                if dist>=j:
                    string = line[i:i+j]
                    if string in letterList[j-3]:
                        number = letterDict[string]
                        if  firstNumber == '':
                            firstNumber = number
                            lastNumber = number
                        else:
                            lastNumber = number
    sum += int(str(firstNumber)+str(lastNumber))
print(sum)

        