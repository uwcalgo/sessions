from sys import stdin
from StringIO import StringIO

S = 0

class node(object):

    def __init__(self,pos,height,nodeNum):
        self.id = nodeNum
        self.position = pos
        self.height = height
        self.canSee = 1 #How many robots before and including this node can see the stage
        self.nodeR = None
        self.nodeL = None

    #Whether the current node can see past the node in front (left) of it
    def canSeeStage(self):
        global S

        if(self.canSeePast(self.nodeL)):
            self.canSee += self.nodeL.canSee

    #Whether this node can see past a given node
    def canSeePast(self,nd):
        global S

        if(nd == None):
            return True

        if((self.height - S)/(self.position) > (nd.height - S)/(nd.position)):
            return True

        return False

    def addRightNode(self,pos,height,nodeNum):
        self.nodeR = node(pos,height,nodeNum)
        self.nodeR.nodeL = self
        return self.nodeR




if(__name__ == "__main__"):

    stdin = StringIO("2\n1.0 3\n1.0 1.1\n2.0 0.9\n3.0 1.0\n2.0 5\n1.0 2.9\n1.2 3.2\n1.4 3.3\n2.0 4.5\n2.2 4.4")
    T = int(stdin.readline())

    for i in range(T):
        S, N = stdin.readline().replace('\n','').split(' ') #Stage height, Number of robots
        S = float(S)
        N = int(N)
        
        xi,yi = stdin.readline().replace('\n','').split(' ')
        Head = node(float(xi),float(yi),0)
        Current = Head
        nodeNum = 1

        for x in range(1,N):
            xi,yi = stdin.readline().replace('\n','').split(' ') #distance from stage, robot height
            Current = Current.addRightNode(float(xi),float(yi),nodeNum)
            nodeNum += 1
            Current.canSeeStage()

        nodes = []
        Current = Head.nodeR        

        #Get all the nodes who are obstructing
        while(Current != None):
            if(Current.canSee == 1):
                nodes.append(Current.nodeL)

            Current = Current.nodeR

        _max = Head

        #Get the node that if removed, has the right not being able to see past the left node
        for nd in nodes:
            if(nd.nodeR.canSeePast(nd.nodeL) and nd.canSee > _max.canSee):
                _max = nd

        print("Case #%d: %d" % (i+1, _max.id))