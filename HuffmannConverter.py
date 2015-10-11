#from OpenSSL import SSL
import FreqNode
import sys
from Crypto.Cipher import AES
import binascii
import random
import re

letterCode={'e':'00000'
,'x':'000010000'
,'z':'000010001'
,'q':'00001001'
,'k':'0000101'
,'j':'0000110'
,'v':'0000111'
,'m':'0001'
,'b':'0010'
,'n':'00110'
,'p':'00111'
,'a':'010'
,'d':'01100'
,'l':'01101'
,'o':'0111'
,'i':'1000'
,'u':'100100'
,'y':'100101'
,'c':'10011'
,'w':'1010'
,'h':'1011'
,'r':'110000'
,'g':'110001'
,'f':'11001'
,'s':'1101'
,'t':'111'
}
if len(sys.argv)<2:
    print "Error input missing"
    print "python HuffmanConverter.py [input]"
    exit()
pt = file(sys.argv[1]).read()
#print "Plaintext:", pt
#print "Pt Hex", pt.encode('hex')
 
key = 'ihavespecialeyes'
pt+= "1"
while(len(pt)%16 !=0):
    pt+="0"

encobj = AES.new(key, AES.MODE_ECB)
ct = encobj.encrypt(pt)
#print "len", len(ct)
#print ct

#print "CipherText:",ct.encode('hex')
#print "\n\n\n"
ctLen = len(ct)*8;
#print ctLen

binStr = '{0:08b}'.format(int(ct.encode('hex'),16))
binStr= "0"*(ctLen-len(binStr))+binStr
#if len(binStr%16)
#print binary_string, len(binary_string)



#binStr=''.join(format(ord(x), 'b') for x in ct)
#print "len", len(binStr)
#print binStr

hTree = FreqNode.genEncoding()
##sampleBinary = "".join(format(ord(x), 'b') for x in sampleNum)
#binStr ='{0:08b}'.format(sampleNum)
def getChar(binaryStr, hTree):
    if len(binaryStr)==0:
        nextTree = hTree.left
        #print nextTree, nextTree.left
        if(nextTree.letter!='!'):
            #print "yo"
            return (nextTree.letter, "")
        return getChar("", nextTree)
    if(binaryStr[0]=='0'):
        #print "left"
        nextTree = hTree.left
        #print nextTree, nextTree.left
        if(nextTree.letter!='!'):
            #print "yo"
            return (nextTree.letter, binaryStr[1::])
        return getChar(binaryStr[1::], nextTree)
    if(binaryStr[0]=='1'):
        #print "right"
        nextTree = hTree.right
        if(nextTree.letter!='!'):
            return (nextTree.letter, binaryStr[1::])
        return getChar(binaryStr[1::], nextTree)
#print binStr, len(binStr)

outStr = ""
binStr+="1"
while 1:
    #print binStr
    (c, binStr)= getChar(binStr, hTree)
    #print binStr
    outStr+=c
    if(not binStr):
        break
#print outStr

nounList = {}
adjList = {}
verbList = {}
def getWordList():
    for line in file("nouns.csv"):
        elem = line.split()[0].lower()
        if not nounList.has_key(elem[0]):
            nounList[elem[0]] = [elem]
        else:
            nounList[elem[0]].append(elem)
    for line in file("adjectives.csv"):
        elem = line.split()[0].lower()
        if not adjList.has_key(elem[0]):
            adjList[elem[0]] = [elem]
        else:
            adjList[elem[0]].append(elem)
    for line in file("ShakespeareWords-verbs.csv"):
        elem = line.split()[0].lower()
        if not verbList.has_key(elem[0]):
            verbList[elem[0]] = [elem]
        else:
            verbList[elem[0]].append(elem)

            

getWordList()
random.seed()
#paragraph = ""
def NVANVAN(firstLetters):
    (l0,l1,l2,l3,l4,l5,l6)= firstLetters[0], firstLetters[1],firstLetters[2],firstLetters[3],firstLetters[4],firstLetters[5],firstLetters[6]
    w0 = random.choice(nounList[l0])
    w1 = random.choice(verbList[l1])
    w2 = random.choice(adjList[l2])
    w3 = random.choice(nounList[l3])
    w4 = random.choice(verbList[l4])
    w5 = random.choice(adjList[l5])
    w6 = random.choice(nounList[l6])
    print "When %s %s, a %s %s doth %s the %s %s." %(w0, w1, w2,w3,w4,w5,w6)
    return "When %s %s, a %s %s doth %s the %s %s." %(w0, w1, w2,w3,w4,w5,w6)
def NANVV1(firstLetters):
    (l0,l1,l2,l3,l4)= firstLetters[0], firstLetters[1],firstLetters[2],firstLetters[3],firstLetters[4]
    w0 = random.choice(nounList[l0])
    w1 = random.choice(adjList[l1])
    w2 = random.choice(nounList[l2])
    w3 = random.choice(verbList[l3])
    w4 = random.choice(verbList[l4])
    print "The %s, being a %s %s, %s and %s." %(w0, w1, w2,w3,w4)
    return "The %s, being a %s %s, %s and %s." %(w0, w1, w2,w3,w4)
def AAN1(firstLetters):
    (l0,l1,l2)= firstLetters[0], firstLetters[1],firstLetters[2]
    w0 = random.choice(adjList[l0])
    w1 = random.choice(adjList[l1])
    w2 = random.choice(nounList[l2])
    print "A %s, %s %s." %(w0, w1, w2)
    return "A %s, %s %s." %(w0, w1, w2)
def NVAN1(firstLetters):
    (l0,l1,l2,l3)= firstLetters[0], firstLetters[1],firstLetters[2],firstLetters[3]
    w0 = random.choice(nounList[l0])
    w1 = random.choice(verbList[l1])
    w2 = random.choice(adjList[l2])
    w3 = random.choice(nounList[l3])
    print "The %s %s a %s %s." %(w0, w1, w2,w3)
    return "The %s %s a %s %s." %(w0, w1, w2,w3)
def VAN1(firstLetters):
    (l0,l1,l2)= firstLetters[0], firstLetters[1],firstLetters[2]
    w0 = random.choice(verbList[l0])
    w1 = random.choice(adjList[l1])
    w2 = random.choice(nounList[l2])
    print "It %s, a %s %s." %(w0, w1, w2)
    return "It %s, a %s %s." %(w0, w1, w2)
def NV1(firstLetters):
    (l0,l1)= firstLetters[0], firstLetters[1]
    w0 = random.choice(nounList[l0])
    w1 = random.choice(verbList[l1])
    print "The %s %s." %(w0, w1)
    return "The %s %s." %(w0, w1)
def N1(firstLetters):
    (l0)= firstLetters[0]
    w0 = random.choice(verbList[l0])
    print "Says the %s." %(w0)
    return "Says the %s." %(w0)

def getOutput(firstLetters ):
    paragraph=""
    grammarStructs = {NVANVAN:7,NANVV1:5, NVAN1:4,AAN1:3,VAN1:3,NV1:2, N1:1}

    while firstLetters:
        wordsLeft = len(firstLetters)
        possibleStructs = []
        for struct in grammarStructs.items():
            if wordsLeft<=2 and struct[1]<=wordsLeft:
                possibleStructs.append(struct[0])
            elif struct[1]<=wordsLeft and struct[1]>2:
                possibleStructs.append(struct[0])
        randomStruct = random.choice(possibleStructs)
        paragraph+=randomStruct(firstLetters)+" "
        firstLetters= firstLetters[grammarStructs[randomStruct]::]
    return paragraph
            


paragraph= getOutput(outStr)
#print "\n\n\n"
#print paragraph