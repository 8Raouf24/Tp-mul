from  part1 import *
from processing_py import *
import time



def readFile(path):
    data = []
    entities = set()
    f = open(path,"r")
    corpus = f.read()
    mat = corpus.replace("\n"," ").split(" ")
    for i in mat:
        entities.add(int(i))
    for i in entities:
        data.append(node(mat.count(str(i)),i))

    return data


def huffman(path):
    nodes = readFile(path)
    
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




huffman("part2.txt")

