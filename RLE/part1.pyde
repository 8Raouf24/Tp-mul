import time

def setup():
    background(25)
    size(1000,800)
    textSize(20);
    op = input('Pgp branche ! Voulez-vous : [1]encoder/[2]decoder: ')
    if op=='1':
        chaine = input('Donnez la chaine a encoder:')
        text('Voici l\'encodage de la chaine '+ chaine +':\n',10,60)
        time.sleep(0.5)
        res = encode(chaine)
        text(res,10,80)
    else :
        chaine = input('Donnez la chaine a decoder:')
        text('Voici le decodage de la chaine '+ chaine +':\n',10,60)
        time.sleep(0.5)
        res = decode(chaine)
        text(res,10,80)
        
    




#Cette fonction nous permet de lire des caractères du clavier via une boite d'aide
def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)


#Fonctiond d'encodage
def encode(chaine):
    i = 0
    fresult = ""
    while i<len(chaine):
     result = ""   
     cpt =1
     j = i
     #Cas de lettre se répetant
     if (j<len(chaine)-2 and chaine[j]==chaine[j+1] and chaine[j]==chaine[j+2]):
         while (j<len(chaine)-1 and chaine[j]==chaine[j+1]):
             cpt+=1
             j+=1
             if  cpt== 2**15:
                 break
         coeff = cpt | 2**15 
         result += hex(coeff)[4:] #On convertit le résultat en hexadecimal
         result += chaine[i]
         i+= cpt
         fresult += result
     else:
            j = i
            cpt =0
            result = ""
            while( j<len(chaine)-1 and ( chaine[j] != chaine[j+1] or chaine[j] != chaine[j+2] )):
                
                result += chaine[j]
                cpt+=1
                j+=1
            #Pour traiter les deux dernieres caractères
            if(i+cpt == len(chaine)-1 ):
                result+=  chaine[-1]
                cpt+= 1

            #On utilise la fonction format pour transformer notre coefficient en hexadecimal et lui ajouter des zéros non significatifs à la fin
            fresult += "{0:#0{1}x}".format(cpt,6)[2:]+result
            i +=cpt 
    return fresult

#Fonction de decodage
def decode(chaine):
    i = 0
    result=""
    while (i<len(chaine)):
        code = chaine[i:i+4]
        val_code = int(code,16)
        #Cas de répétition
        if val_code>2**15:
            coeff = val_code -32768
            for j in range (coeff):
                result+= chaine[i+4]
            i +=5
            
        else:
            #Cas de non répétition
            coeff = val_code
            result+= chaine[i+4:i+4+coeff]
            i +=coeff+4
    return result
