from collections import Counter

def populateMatrix(fileName): #File name as a string .txt included
    matrixData = open(fileName,"r")
    matrix = []
    for i in matrixData:
        toAppend = ''.join(i.split())
        matrix.append(toAppend)
    return matrix

def getPartialProfile(fileName): ##returns the profile without doing any counting
    profiles = []
    matrix = list(populateMatrix(fileName))
    profileLen = len(matrix)
    for i in range(len(matrix[0])):
        toAppend = ""
        single_profile = ""
        for j in range(profileLen):
            single_profile = single_profile +(matrix[j][i])
        toAppend = ''.join(single_profile.split())
        profiles.append(toAppend)
    return profiles

def getSymbol(index):
    options = {0: "A", 1: "C", 2: "G",3:"T"}
    return options[index]

def getProfile(fileName): ##returns the count of each character(ACGT) from the partial string
    profiles = list(getPartialProfile(fileName))
    profileCount = []
    finalProfile= []
    DNA = ["A","C","G","T"]
    
    for i in profiles:
        profileCount = []
        for j in DNA:
            profileCount.append(i.count(j))
        finalProfile.append(profileCount)
        
    return finalProfile 
            
def printProfile(fileName): ##prints the profile in the form asked by the website.Done in a seperate function as getConsensus needs some data from the getProfile
    profile = list(getProfile(fileName))
    profile = [["A: ","C: ","G: ","T: "]] + profile
    for i in range(len(profile[0])):
        toPrint = []
        for j in range(len(profile)):
            toPrint.append(profile[j][i])
        for z in toPrint:
            print(str(z) + " ", end = '')
        print("")

def getConsensus(fileName): ##returns the consensus using the data from the getProfile function
    profile = list(getProfile(fileName))
    consensus = ""
    for i in profile:
        highestIndex = i.index(max(i))
        consensus = consensus + getSymbol(highestIndex)
    return consensus

print(getConsensus("test1.txt"))
printProfile("test1.txt")

