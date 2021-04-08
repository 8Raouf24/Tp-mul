from processing_py import *
import time



pos1=600
pos2=200

def count(string):
    liste = []
    seta = set(string)
    for i in seta:
        liste.append(node(string.count(i),i))
    return liste

class node:
    def __init__(self, freq, sign, left=None, right=None):
        # frequency of symbol
        self.freq = freq
 
        # symbol name (charecter)
        self.sign = sign
 
        # node left of current node
        self.left = left
 
        # node right of current node
        self.right = right
 
        # tree direction (0/1)
        self.direction = ''



def drawNodes(node,pos1,pos2):
    # huffman code for current node
    # global pos1
    # global pos2
    if (node!=None):
        if( node.left and  node.right):
            time.sleep(1)
            app.fill(255)
            app.ellipse(pos1, pos2, 70, 30)
            app.fill(0)
            app.text(str(node.freq),pos1-10,pos2)    
            i = pos1-4
            j = pos2+12

            x = pos1 - 100
            y = pos2 + 100
            # app.stroke(127)
            app.fill(0)
            app.line(i,j,x,y)
            app.text("0",((i+x)/2)-5,((j+y)/2)-5)
            app.redraw()
            drawNodes(node.left,x,y)

            x = pos1 + 100
            y = pos2 + 100
            app.line(i, j, x, y)
            app.fill(50)
            app.text("1", ((i + x) / 2)+5, ((j + y) / 2)-5)
            app.redraw()
            drawNodes(node.right,x,y)
        else:
                time.sleep(1)
                app.fill(255)
                app.ellipse(pos1, pos2, 70, 30)
                app.fill(0)
                app.text(node.sign+" || "+str(node.freq),pos1-10,pos2)
                app.redraw()
        
       
    #print(cpt)


def huffman(chaine):
    nodes = count(chaine)
    
    while len(nodes) > 1:
        # sort all the nodes in ascending order
        # based on theri frequency
        nodes = sorted(nodes, key=lambda x: x.freq)
    
        # pick 2 smallest nodes
        left = nodes[0]
        right = nodes[1]
    
        # assign directional value to these nodes
        left.direction = 0
        right.direction = 1
    
        # combine the 2 smallest nodes to create
        # new node as their parent
        newNode = node(left.freq+right.freq, left.sign+right.sign, left, right)
    
        # remove the 2 nodes and add their
        # parent as new node among others
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    
    # Huffman Tree is ready!

    drawNodes(nodes[0],600,200)

app=App(1200,1000)
app.background(224,217,234)
app.redraw()
time.sleep(3)
huffman('aaaabsssshe')
time.sleep(10)
app.exit()