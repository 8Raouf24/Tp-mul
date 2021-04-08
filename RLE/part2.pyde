c = True
img = None



def binarize(img):
    for i in range(0,img.height*img.width,1):
        if brightness(img.pixels[i])>127 :
            img.pixels[i]=color(255)
        else:
            img.pixels[i]=color(0)
    img.updatePixels()


def encode(img):
    f=open("encode.txt","w")
    i = 0
    fresult = ""
    while i<len((img.pixels)):
        result = ""  
        cpt =1
        j = i
        if (j<len(img.pixels)-2 and brightness(img.pixels[j])==brightness(img.pixels[j+1]) and brightness(img.pixels[j])==brightness(img.pixels[j+2])):
            while (j<len(img.pixels)-1 and brightness(img.pixels[j])==brightness(img.pixels[j+1])):
                cpt+=1
                j+=1
                if  cpt== 2**15:
                    break
            coeff = cpt | 2**15 
            result += hex(coeff)[2:]
            if brightness(img.pixels[j]) == 255:
               result += "FF"
            else :
                result += "00"
            i+= cpt
            fresult+=result
            f.write("iteration\n")
            f.write(result+" ")
        else:
            j = i
            cpt =0
            result = ""
            while( j<len(img.pixels)-1 and ( img.pixels[j] != img.pixels[j+1] or img.pixels[j] != img.pixels[j+2] )):

                if brightness(img.pixels[j]) == 255:
                    result += "FF"
                else :
                    result += "00"
                cpt+=1
                j+=1
            #Pour traiter les deux dernieres caractères
            if(i+cpt == len(img.pixels)-1 ):
                
                if brightness(img.pixels[j]) == 255:
                    result += "FF"
                else :
                    result += "00"
                cpt+= 1
            fresult += "{0:#0{1}x}".format(cpt,6)[2:]+result+' '
            f.write("iteration\n")
            f.write(fresult)
            i +=cpt 
    c = False

def save(data,filename):
    result=""
    for i in data:
        result+=chr(i);
    saveBytes(filename,result)

def setup():
    size(600,600)
    background(0)
    img=loadImage("part2.jpg")
    img.filter(GRAY)
    image(img,300,0)
    binarize(img)
    print(img.pixels)
    encode(img)
        


  
