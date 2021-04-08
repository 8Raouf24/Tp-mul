import time

def setup():
    background(255)
    size(1200,800)
    img1 = loadImage("./data/frame1.png")
    image(img1, 0, 0)
    
position = []

bright_c1 = []
cr = {}
cv = {}
diff = 40
fait = False
value_mse = []

def draw():
    global bright_c1 
    global cr
    global cv
    global diff
    global fait
    global value_mse
    #D'abord nous effectuons deux clicks afin de générer notre carré rouge et notre carré vert 
    if len(position)==2 and fait==False:

        #Nous commencons par créer notre carré rouge en cliquant sur les deux extremités du carré 
        
        #Afin de mieux structurer nos données, nous avons utiliser un dictionnaire pour stocker les coordonées du point de départ du carré, ainsi que sa longueur et sa largeur
        cr = {"x_cr":position[0][0],"y_cr":position[0][1],"h_cr":abs(position[0][0]-position[1][0]),"w_cr":abs(position[0][1]-position[1][1])}
        noFill()
        stroke(255,0,0)
        rect(cr["x_cr"],cr["y_cr"],cr["h_cr"],cr["w_cr"])
        #Nous générons une liste contenant les valeurs de luminosité de chaque pixels de notre carré rouge
        c1 = get(cr["x_cr"],cr["y_cr"],cr["h_cr"],cr["w_cr"])
        loadPixels()
        for i in range (cr["h_cr"]*cr["w_cr"]):
            bright_c1.append(brightness(pixels[i]))
        print(len(bright_c1))
        stroke(0,255,0)
        fait =True
        
        #Nous créeons notre carré vert
        
        rect(cr["x_cr"]-diff,cr["y_cr"]-diff,cr["h_cr"]+diff*2,cr["w_cr"]+diff*2)
        noLoop()
        loop()
        
    #Puis le 3ème clique activera la comparaison
    if len(position)==3:
        #Une fois les deux carrés prets, nous passons à la seconde image
        img2 = loadImage("./data/frame2.png")
        image(img2, 0, 0)
        """stroke(255,0,0)
        rect(cr["x_cr"],cr["y_cr"],cr["h_cr"],cr["w_cr"])"""
        stroke(0,255,0)
        #Nous redessinons notre carré vert
        cv={"x_cv":cr["x_cr"]-diff,"y_cv":cr["y_cr"]-diff,"h_cv":cr["h_cr"]+diff*2,"w_cv":cr["w_cr"]+diff*2}
        rect(cv["x_cv"],cv["y_cv"],cv["h_cv"],cv["w_cv"])
        
        #Nous appellons la fonction carre_list, afin de générer tout les carrés rouges existants dans notre carrés vert
        noLoop()
        list_carre = carre_list(cv,cr,5)
        
        
        #Puis nous utilisions la fonction compare_carre pour calculer l'erreur quadratique moyenne et ainsi localiser le carré contenant le pieton 
        value_mse = compare_carre(bright_c1,list_carre)
        
        print("Le carre du pieton commence a la position:",value_mse[0][0])
        loop()
    #Enfin le 4eme clique displayera le carré le plus ressemblant
    if len(position)==4:
        img2 = loadImage("./data/frame2.png")
        image(img2, 0, 0)
        stroke(255,0,0)
        rect(value_mse[0][0][0],value_mse[0][0][1],cr["h_cr"],cr["w_cr"])
        
        
    
    

        
        
    
#Cette fonction retrounera une liste de tuples, le 1 er element du tuple sera les coordonnées du carré traité, et le deuxieme élement sera une liste des valeurs de la luminosité de chaque pixels
#Nous donnons en paramètre le carré vert ( le grand carré ) et le carré rouge ( le petit carré ) ainsi que la valeur de delta ( combien nous voulons extraire de carré rouge du carré vert, ce n'est pas exactement delta mais c'est un coefficient fait dans ce but )  
def carre_list(carrev,carrer,delta):
    global cr
    global cv
    vect = []
    cpt = 0
    j = 0
    for i in range (((diff*2)/delta+1)**2):
        temp = []
        carre_temp={"x_ct":cv["x_cv"]+cpt,"y_ct":cv["y_cv"]+j,"h_ct":cr["h_cr"],"w_ct":cr["w_cr"]}
        
        
        stroke(255,0,0)
        rect(carre_temp["x_ct"],carre_temp["y_ct"],carre_temp["h_ct"],carre_temp["w_ct"])
        c_temp = get(carre_temp["x_ct"],carre_temp["y_ct"],carre_temp["h_ct"],carre_temp["w_ct"])
        c_temp.loadPixels()
    
        for i in range (carre_temp["h_ct"]*carre_temp["w_ct"]):
            temp.append(brightness(c_temp.pixels[i]))
        vect.append({"x,y":(carre_temp["x_ct"],carre_temp["y_ct"]),"brightness":temp})
            
        if carre_temp["x_ct"]+carre_temp["h_ct"] == cv["x_cv"]+cv["h_cv"] :
            cpt = 0
            j += delta
        else:
            cpt+=delta
        
        

    return vect
    
  
def compare_carre(co,list_c):
    cmp = []
    for i in list_c:
        cmp.append((i["x,y"],(mse(co,i["brightness"]))))
    cmp.sort(key=lambda x:x[1])
    return cmp

def mouseClicked(): 
    global position
    position.append((mouseX,mouseY))
    print(position)
    
def mse( target, x):
    temp = 0
    for i in range(len(target)):
        temp +=(target[i]-x[i])**2
    return temp/len(target)
