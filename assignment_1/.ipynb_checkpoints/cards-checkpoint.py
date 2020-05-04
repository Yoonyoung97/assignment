import sys

def assignment(path):
    inp = open(path, "r")
    count = int(inp.readline().rstrip('\n'))
    out = open("./cards.out", "w")
    iterator = 1
    nofChange = 0
    isChange = False

    while nofChange !=2:
        isChange = False
        inp = open(path, "r")
        inp.readline()
        for i in range(count):
            data = inp.readline()
            if not data:
                break
            else:
                data = int(data.rstrip('\n'))
                if iterator == data:
                    iterator+=1
                    isChange = True
        if not isChange:
            #print("Append :: " + str(iterator))
            out.write(str(iterator)+'\n')
            iterator+=1
            nofChange+=1
if __name__ == "__main__":
    assignment("./cards.inp")
    #print(sys.argv[1])
    
    
 