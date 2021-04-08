import time

def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)



def setup():
    background(150)
    size(1000,800)
    textSize(20);
    op = input('Quel chaine tu veux encoder morray ? ')
    #text('Voici l\'arbre Huffman de la chaine ',10,23)
    #time.sleep(0.5)
    
 
def draw():
    noFill()
    ellipse(600, 600, 100, 55)
    
    fill(255, 102, 153, 51)
    text('f | 5',580,610)
    fill(0, 102, 153, 51)
    stroke(255,0,0)
    line(600, 570, 550, 540)
    text('1',570,540)
    
