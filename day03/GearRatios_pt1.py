def fn_file():
    # file = open("sourcefile.txt", mode="r")
    file = open("C:\\Users\\laura.velez\\source\\repos\\AdventOfCode_Python\\day03\\sourcefile.txt", mode="rt")
    # file = open("C:\\Users\\laura.velez\\source\\repos\\AdventOfCode_Python\\day03\\t2.txt", mode="rt")
    # file = open("C:\\Users\\laura.velez\\source\\repos\\AdventOfCode_Python\\day03\\training.txt", mode="rt")
    f = []
    for line in file:
        line = line.replace("\n", "")
        line = line.replace("\r", "")
        line = line.replace("\t", "")
        f.append(list(line))
    file.close()
    return f

def fn_file2(f):
    x = []
    dicc = []
    num = '0'
    b = False
    n = ''
    for line in f:
        m = []           
        for char in line:            
            if char.isdigit():
                m.append(num)
                b = True
                n = n + char
            elif(not(char.isdigit()) and (b)):   
                dicc.append(n)             
                num = str(int(num) + 1)
                m.append(char)
                b = False  
                n = ''             
            else:
                m.append(char)
                b = False        
        x.append(m)
    return x, dicc

def fn_neighbors(x,y,f2):
    p = []
    for n in range(-1,2):                    
        i = x + n
        for m in range(-1,2):
            j = y + m
            find = str(f2[i][j])
            if(find.isdigit() and not(p.__contains__(find))):
                p.append(find)
    return p

def fn_gears():
    f = fn_file()
    f2, dicc = fn_file2(f)
    # print(f2)
    sum = 0
    p = []
    sumar = []
    x = 0
    # for ln in f2:
    #     # print(ln)
    #     y = 0
    #     for char in ln:
    #         if((str(char) != '.') and (not(str(char).isdigit()))):                
    #             i = x
    #             j = y
    #             for n in range(-1,2):                    
    #                 i = x + n
    #                 for m in range(-1,2):
    #                     j = y + m
    #                     find = str(f2[i][j]) # me jode por que solo toma 1 cajón, si el num del dicc se compone de 2 o más como llave, F
    #                     if(find.isdigit() and not(p.__contains__(find))):
    #                         p.append(find)
    #         y = y + 1
    #     x = x + 1

    for ln in range(0,len(f2)):
        # print(f2[ln])
        y = 0
        for char in range(0,len(f2[ln])):
            if((f[ln][char] != '.') and (not(f[ln][char].isdigit()))):                
                i = x
                j = y
                for n in range(-1,2):                    
                    i = (x + n) if (x + n) < len(f2) else x
                    for m in range(-1,2):
                        j = (y + m) if (y + m) < len(f2[ln]) else y
                        find = str(f2[i][j]) # me jode por que solo toma 1 cajón, si el num del dicc se compone de 2 o más como llave, F
                        if(find.isdigit() and not(p.__contains__(find))):
                            p.append(find)
                            sumar.append(int(find))
            y = y + 1
        x = x + 1

    sumar.sort()
    for id in sumar:
        print(dicc[id])
        sum = sum + int(dicc[id])
    
    print(sum)


fn_gears()