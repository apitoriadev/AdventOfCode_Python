class Game:
    def __init__(self, id, set, red, green, blue, possible):
        self.id = id
        self.set = set
        self.red = red
        self.green = green
        self.blue = blue
        self.possible = possible

def main_fn():
    redOG, greenOG, blueOG = 12, 13, 14
    file = open("C:\\Users\\laura.velez\\source\\repos\\AdventOfCode_Python\\day02\\sourcefile.txt", mode="r")    
    ids = []
    gameListAll = [] 
    lines = 0   
    for line in file:
        lines = lines + 1
        line = line.replace("\n", "")
        first = line.split(': ')
        id = first[0].split('Game ')[1]
        second = first[1].split('; ')
        set = 1
        print(id)
        print(second)
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
                redValue = val[0]
                possibleR = True if redOG >= int(redValue) else False
            else:
                redValue = 0
                possibleR = True
            if(blue):
                index = 0
                for color in setSplit:
                    if(color.__contains__('blue')):
                        break
                    else:
                        index = index + 1            
                val = setSplit[index].split(' ')
                blueValue = val[0]
                possibleB = True if blueOG >= int(blueValue) else False
            else:
                blueValue = 0
                possibleB = True
            if(green):
                index = 0
                for color in setSplit:
                    if(color.__contains__('green')):
                        break
                    else:
                        index = index + 1            
                val = setSplit[index].split(' ')
                greenValue = val[0]
                possibleG = True if greenOG >= int(greenValue) else False
            else:
                greenValue = 0
                possibleG = True
            possibleSet = True if (possibleB == possibleG == possibleR) else False
            game = Game(id,set,redValue,greenValue,blueValue,possibleSet)
            gameListAll.append(game)     
            set = set + 1


main_fn()