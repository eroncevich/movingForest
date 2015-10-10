#from OpenSSL import SSL
import FreqNode
import sys
from Crypto.Cipher import AES
import binascii

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
if len(sys.argv)<2:
    print "Error input missing"
    print "python HuffmanConverter.py [input]"
    exit()
pt = file(sys.argv[1]).read()
print "Plaintext", pt
print "Pt Hex", pt.encode('hex')
 
key = 'ihavespecialeyes'
pt+= "1"
while(len(pt)%16 !=0):
    pt+="0"
print pt
 
encobj = AES.new(key, AES.MODE_ECB)
ct = encobj.encrypt(pt)
#print "len", len(ct)
#print ct

print "CipherText",ct.encode('hex')
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
        return ('!',"")
    if(binaryStr[0]=='0'):
        #print "left"
        nextTree = hTree.left
        if(nextTree.letter!='!'):
            return (nextTree.letter, binaryStr)
        return getChar(binaryStr[1::], nextTree)
    if(binaryStr[0]=='1'):
        #print "right"
        nextTree = hTree.right
        if(nextTree.letter!='!'):
            return (nextTree.letter, binaryStr)
        return getChar(binaryStr[1::], nextTree)
print binStr, len(binStr)

outStr = ""
while 1:
    (c, binStr)= getChar(binStr, hTree)
    outStr+=c
    if(c=='!'):
        break
print outStr
