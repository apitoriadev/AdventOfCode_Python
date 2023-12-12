def main_fn():    
    # file = open("sourcefile.txt", mode="r")   
    file = open("C:\\Users\\laura.velez\\source\\repos\\AdventOfCode_Python\\day02\\sourcefile.txt", mode="r")   
    pow = 0
    for line in file:
        redOG, greenOG, blueOG = 0,0,0
        line = line.replace("\n", "")
        first = line.split(': ')
        id = first[0].split('Game ')[1]
        second = first[1].split('; ')
        for gSet in second:
            red = gSet.__contains__('red')
            blue = gSet.__contains__('blue')
            green = gSet.__contains__('green')
            setSplit = gSet.split(', ')
            if(red):
                index = 0
                for color in setSplit:
                    if(color.__contains__('red')):
                        break
                    else:
                        index = index + 1            
                val = setSplit[index].split(' ')
                redValue = int(val[0])
            else:
                redValue = 0
            if(blue):
                index = 0
                for color in setSplit:
                    if(color.__contains__('blue')):
                        break
                    else:
                        index = index + 1            
                val = setSplit[index].split(' ')
                blueValue = int(val[0])
            else:
                blueValue = 0
            if(green):
                index = 0
                for color in setSplit:
                    if(color.__contains__('green')):
                        break
                    else:
                        index = index + 1            
                val = setSplit[index].split(' ')
                greenValue = int(val[0])
            else:
                greenValue = 0
            redOG = redOG if redOG > redValue else redValue
            greenOG = greenOG if greenOG > greenValue else greenValue
            blueOG = blueOG if blueOG > blueValue else blueValue
        pow = pow + (redOG * greenOG * blueOG)
    print(pow)

main_fn()