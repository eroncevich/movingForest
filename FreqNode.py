import operator
import freqNode
letterFreq = {'a':11.602, 'b':4.702, 'c':3.511 ,'d':2.670,'e':2.007,'f':3.779,
'g':1.950,'h':7.232,'i':6.286,'j':0.597,'k':0.590,'l':2.705,'m':4.383,'n':2.365,
'o':6.264,'p':2.545,'q':0.173,'r':1.653,'s':7.755,'t':16.671,'u':1.487,'v':0.649,
'w':6.753,'x':0.017,'y':1.620,'z':0.034}

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

sortedFreq= sorted(letterFreq.items(), key=operator.itemgetter(1))

def genEncoding():
    #print sortedFreq
    fn = freqNode('a',12)
    #freqNodes =[]
    freqNodes = [freqNode(sortedFreq[i][0],sortedFreq[i][1]) for i in range(0,len(sortedFreq))]
    hTree =genTree(freqNodes)
    #print hTree.freq

    #printTree(hTree, "")
    return hTree
    ##print freqNodes

def printTree(hTree, code):
    #print "Current Code:", code
    #print str(hTree)
    if(hTree.letter!="!"):
        print hTree.letter, code
    if hTree.left!=-1:
        printTree(hTree.left, code+'0')
    if hTree.right!=-1:
        #print "hey"
        printTree(hTree.right, code+'1')

def genTree(freqList):
    if len(freqList)==1:
        return freqList[0]
    node1 = freqList[0]
    node2= freqList[1]
    #print node1,node2
    newFreq = node1.freq+node2.freq
    fn = freqNode('!', newFreq)
    fn.addChildren(node1,node2)
    inserted = False
    for i in range(2,len(freqList)):
        if freqList[i].freq>newFreq:
            freqList.insert(i,fn)
            inserted = True
            break
    if inserted==False:
        freqList.append(fn)

    return genTree(freqList[2::])

class freqNode(object):
    left = -1
    right =-1
    def __init__(self, letter, freq):
        self.letter = letter
        self.freq = freq
        #print letter, freq
    def addChildren(self,left, right):
        self.left = left
        self.right = right
    def __str__(self):
        return "(%s,%f)"%(self.letter,self.freq)