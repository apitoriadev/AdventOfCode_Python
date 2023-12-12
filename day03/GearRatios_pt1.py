def fn_file():
    # file = open("sourcefile.txt", mode="r")
    file = open("C:\\Users\\laura.velez\\source\\repos\\AdventOfCode_Python\\day03\\sourcefile.txt", mode="rt")
    f = []
    for line in file:
        line = line.replace("\n", "")
        line = line.replace("\r", "")
        line = line.replace("\t", "")
        f.append(list(line))
    file.close()
    return f

def fn_gears():
    f = fn_file
    save = []
    for ln in f: 
        x = f.index(ln)    
        y = 0   
        for l in ln:
            if((l != '.') and (not(l.isdigit()))):
                s = []
                s.append(int(x))
                s.append(int(y))
                save.append(s)
            y = y + 1          
        
    print(1)


fn_gears()