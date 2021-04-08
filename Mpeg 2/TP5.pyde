blocs = []    
point = None
img1 = None 
img2 = None
img3 = None
start = False 
w_rect = None
h_rect = None
position = []
bright_c1 = []
delta = 1

def setup():
    global img
    global bloc
    global img1
    global img2
    img=loadImage("frame2.png")
    img.loadPixels()
    img2=loadImage("frame1.png")
    img.loadPixels()
    size(512,512)
    for i in range(0,img.width,16):
        for j in range(0,img.height,16):
            bloc.append((i,j,img.get(i,j,16,16)))
    search()
    
    
    


def draw():
    pass
    
    
def MSE(frame1,crocop):
    longeur=16
    largeur=16
    
    MSE=0
    frame1.loadPixels()
    crocop.loadPixels()

    
    for x in range(largeur*longeur):
    
            MSE+=(brightness(crocop.pixels[x])-brightness(frame1.pixels[x]))**2
        
    MSE=MSE/(longeur*largeur)

    return MSE  

def diff(bloc1,bloc2):
    bloc1.loadPixels()
    bloc2.loadPixels()
    for i in range(256):
        bloc1.pixels[i]=bloc1.pixels[i]-bloc2.pixels[i]
    return bloc1
              
def search():
    global  bloc
    global delta
    global img1
    global img2
    global img3
    for i in bloc:
       x=i[0]
       y=i[1]
       z=i[2]
       mse=100000000
       best=None
       _pos1=0
       _pos2=0
       for pos1 in range(-delta,delta):
           for pos2 in range(-delta,delta):
               if x+pos1>0 and y+pos2>0:
                   #calcule de mse
                   _img=img2.get(x+pos1,y+pos2,16,16)
                   if mse>MSE(z,_img):
                       mse=MSE(z,_img)
                       best=_img
                       _pos1=x+pos1
                       _pos2=y+pos2
       if best!=None:
           best=dif(best,z)
           image(best,x,y)
           print(_pos1,_pos2,best)

       

   
