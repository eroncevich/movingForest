import sys
import re
from Crypto.Cipher import AES

if len(sys.argv)<2:
    print "Error input missing"
    print "python HuffmanDecrypt.py [input]"
    exit()
paragraph = file(sys.argv[1]).read()
#print "Input:", paragraph
#print "Pt Hex", pt.encode('hex')
 
key = 'ihavespecialeyes'


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


def reverseParagraph(paragraph):
    lines = paragraph.split(".")
    firstChars = ""
    for line in lines:
        m = re.search('When .* .*, a .* .* doth', line)
        if m:
            words = line.split()
            (l0,l1,l2,l3,l4,l5,l6) = words[1],words[2],words[4],words[5],words[7],words[9],words[10]
            firstChars+= l0[0]+l1[0]+l2[0]+l3[0]+l4[0]+l5[0]+l6[0]
            continue
        m = re.search('The .* being a .*,', line)
        if m:
            words = line.split()
            (l0,l1,l2,l3,l4) = words[1],words[4],words[5],words[6],words[8]
            firstChars+= l0[0]+l1[0]+l2[0]+l3[0]+l4[0]
            continue
        m = re.search('The .* .* a .* .*', line)
        if m:
            words = line.split()
            (l0,l1,l2,l3) = words[1],words[2],words[4],words[5]
            firstChars+= l0[0]+l1[0]+l2[0]+l3[0]
            continue
        m = re.search('A .*, .* .*', line)
        if m:
            words = line.split()
            (l0,l1,l2) = words[1],words[2],words[3]
            firstChars+= l0[0]+l1[0]+l2[0]
            continue
        m = re.search('It .*, a .* .*', line)
        if m:
            words = line.split()
            (l0,l1,l2) = words[1],words[3],words[4]
            firstChars+= l0[0]+l1[0]+l2[0]
            continue
        m = re.search('The .* .*', line)
        if m:
            words = line.split()
            (l0,l1) = words[1],words[2]
            firstChars+= l0[0]+l1[0]
            continue
        m = re.search('Says the .*', line)
        if m:
            words = line.split()
            l0 = words[2]
            firstChars+= l0[0]
            continue
    return firstChars


firstChars =reverseParagraph(paragraph)
#print firstChars

def reverseHuffmann(firstChars):
    binStr = ""
    for c in firstChars:
        binStr+=str(letterCode[c])
    return binStr[0:[m.start(0) for m in re.finditer("10*$", binStr)][0]]


binStr = reverseHuffmann(firstChars)
ct = hex(int(binStr,2))
ct = ct[2:len(ct)-1]
print "Decrypted CipherText:", ct,"\n\n"
ct = ct.decode('hex')

encobj = AES.new(key, AES.MODE_ECB)
pt = encobj.decrypt(ct)

pt =pt[0:[m.start(0) for m in re.finditer("10*$", pt)][0]]
print "Decrypted Plaintext:",pt
    
#print nounList
#print adjList
#print verbList
#print paragraph