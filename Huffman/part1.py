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


def printNodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.direction)
    cpt = 1
    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        cpt+=1
        printNodes(node.left, newVal)
    if(node.right):
        cpt+=1
        printNodes(node.right, newVal)
 
        # if node is edge node then
        # display its huffman code
    if(not node.left and not node.right):
        
        print(f"{node.sign},{node.freq} -> {newVal}")
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

    printNodes(nodes[0])

huffman('babzadaz')