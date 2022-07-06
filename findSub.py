def findSub(sub, string):
    #print(sub,string)
    if len(sub) == 0 or len(string) == 0: 
        return 0
    cnt = 0
    for idx, ch in enumerate(string):
        s = string[idx:idx+len(sub)]
        if s == sub :
            #print(s, sub)
            cnt += 1
    return cnt            
         
def isVowel(ch):
    if ch in ('A', 'E', 'I', 'O', 'U'):
        return True
    else:
        return False

def addMap(origString, string, targetMap):
    for jdx in range(len(string)):
        subString = string[:jdx+1]
        if subString in targetMap:
            pass
        else:
            targetMap[subString] = findSub(subString, origString)
        if subString not in targetMap:
            break
    
def minion_game(string):
    # if stirng = "", there is no winner
    if len(string) == 0:
        return "Draw"
    stuartMap = {}
    kevinMap = {}
    for idx, ch in enumerate(string):
        if isVowel(ch):
            addMap(string, string[idx:], kevinMap)
        else:
            addMap(string, string[idx:], stuartMap)
            
   #sum of Kevin's
    kSum = 0
    for i in list(kevinMap.values()):
        kSum += i
    sSum = 0
    for j in list(stuartMap.values()):
        sSum += j
    #print(kevinMap, kSum)    
    #print(stuartMap, sSum)
    
    returnStr = ""
    if sSum == kSum:
        returnStr = "Draw"
    elif sSum > kSum:
        returnStr = f"Stuart %d" % sSum
    else:
        returnStr = f"Kevin %d" % kSum
    print(stuartMap)
    print(returnStr)
    return returnStr

print(findSub("ANA", "BANANA"))
print(findSub("S", "BAANANAS"))

s1 = "NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANA"
print(findSub("NA", s1))
print(s1.count("NA"))