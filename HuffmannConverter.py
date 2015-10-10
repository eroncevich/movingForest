import FreqNode
letterCode={'e':00000
,'x':000010000
,'z':000010001
,'q':00001001
,'k':0000101
,'j':0000110
,'v':0000111
,'m':0001
,'b':0010
,'n':00110
,'p':00111
,'a':010
,'d':01100
,'l':01101
,'o':0111
,'i':1000
,'u':100100
,'y':100101
,'c':10011
,'w':1010
,'h':1011
,'r':110000
,'g':110001
,'f':11001
,'s':1101
,'t':111
}

#sampleNum = 923903290329803428904
sampleNum = 0x9329048904308932489fde

hTree = FreqNode.genEncoding()
##sampleBinary = "".join(format(ord(x), 'b') for x in sampleNum)
binStr ='{0:08b}'.format(sampleNum)
def getChar(binaryStr, hTree):
    if len(binaryStr)==0:
        return ('!',"")
    if(binaryStr[0]=='0'):
        print "left"
        nextTree = hTree.left
        if(nextTree.letter!='!'):
            return (nextTree.letter, binaryStr)
        return getChar(binaryStr[1::], nextTree)
    if(binaryStr[0]=='1'):
        print "right"
        nextTree = hTree.right
        if(nextTree.letter!='!'):
            return (nextTree.letter, binaryStr)
        return getChar(binaryStr[1::], nextTree)
print binStr

outStr = ""
while 1:
    (c, binStr)= getChar(binStr, hTree)
    outStr+=c
    if(c=='!'):
        break
print outStr

#for i in range(0,len(sampleBinary)):
