#problem: http://rosalind.info/problems/cons

def read(path):
    length = 0

    with open(path, 'r') as file:       #get dna length
        file.readline()

        while(True):
            line = file.readline().replace("\n", "")
            
            if(line[0] == ">"):
                break

            length += len(line)

    dna = {                             #initialize dictionary
            "A" : [0]*length,
            "C" : [0]*length,
            "T" : [0]*length,
            "G" : [0]*length
        }
   
    with open(path, 'r') as file:       #runs through the data
        for line in file:

            if(line[0] == ">"):
                x = 0
                continue

            line = line.replace("\n","");
            dnaLen = len(line)           

            for i in xrange(dnaLen):    #puts bases into array
                base = line[i]                
                dna[base][x] += 1
                x += 1

        A = dna["A"]
        C = dna["C"]
        T = dna["T"]
        G = dna["G"]
        res = []

        for i in xrange(length):        #gets highest occuring base for each column
            highest = getHighest([C[i],"C"], [A[i],"A"])
            highest = getHighest([T[i],"T"], [highest[0],highest[1]])
            highest = getHighest([G[i],"G"], [highest[0],highest[1]])
            res.append(highest)

        return [res, dna]

def getHighest(A,B):
    if(A[0] > B[0]):
        return A
    return B

def display(res, out):
    pr = ""
    
    for i in res:
        pr += i[1] + " "

    print(pr)

    with open(out, 'w') as file:
        file.writelines(pr)
        file.writelines("\n")

def displayProfile(dna, out):
    stop = len(dna["A"])

    with open(out, 'a') as file:        
        for i in dna:
            print("%s " % i),
            file.write("%s " % i)
            b = dna[i]

            for x in xrange(stop):
                print("%i " % b[x]),
                file.writelines("%i " % b[x])

            print
            file.writelines("\n")
        

if (__name__ == "__main__"):
    res = read(".\\cons\\rosalind_cons.txt");
    display(res[0], ".\\cons\output.txt")
    displayProfile(res[1], ".\\cons\output.txt")