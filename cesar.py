import string

def position(x):
    alphabet = string.ascii_lowercase 
    if x in alphabet :
     return alphabet.index(x)
    else :
      return -1

def decalage(x, n):
    alphabet = string.ascii_lowercase
                                                        
           
    if x == string.punctuation or x == "" or x == ",":
        return ""
    elif x =="é" or x=="è":
        pos = (position("e") + n) % 26                      
        return alphabet[pos]
    elif x =="a" or x=="à":
        pos = (position("a") + n) % 26                      
        return alphabet[pos]
    pos = (position(x) + n) % 26                         
    return alphabet[pos]

def cesar_codage(n, texte):
   
    alphabet = string.ascii_lowercase
    resultat = ""  
    
    for c in texte :
            resultat += decalage(c, n)  

    return resultat
def cesar_decodage(n, texte):
    alphabet = string.ascii_lowercase
    resultat = ""  
    
    for c in texte :
            resultat += decalage(c, -n)  
        
    return resultat


message = "Là sécurité est une fonction incontournable des réseaux de, communication"
message = message.lower()
cle_cesar = 13  
message_chiffre = cesar_codage(cle_cesar, message)
message_dechiffre = cesar_decodage(cle_cesar, message_chiffre)

print("chiffré :", message_chiffre)
print("déchiff :", message_dechiffre)
print(position('3'))