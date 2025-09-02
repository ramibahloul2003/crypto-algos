import string


def position(x):
    alphabet = string.ascii_lowercase
    if x in alphabet :
     return alphabet.index(x)
    else :
      return -1

def decalage(x, n):
    alphabet = string.ascii_lowercase
                                                        
           
    if x == string.punctuation or x == " ":
        return ""
    elif x =="é" or x=="è":
        pos = (position("e") + n) % 26                      
        return alphabet[pos]
    pos = (position(x) + n) % 26                           
    return alphabet[pos]

def vigenere_coder(texte, cle):
   
    alphabet = string.ascii_lowercase
    texte = texte.lower()
    cle = cle.lower()
    texte_code = ""
    
    for i, c in enumerate(texte):
        if c in alphabet:
            decal = position(cle[i % len(cle)])
            texte_code += decalage(c, decal)
        
    return texte_code

def vigenere_decoder(texte_code, cle):
   
    alphabet = string.ascii_lowercase
    texte = ""
    cle = cle.lower()

    for i, c in enumerate(texte_code):
        if c in alphabet:
            decal = position(cle[i % len(cle)])
            texte += decalage(c, -decal)    

    return texte

texte = "le chiffrement est ,utile"
cle ="azerty"    
result=vigenere_coder(texte, cle)
message_dechiffre = vigenere_decoder(result , cle)

print("chiffré :", result)
print("déchiff :", message_dechiffre)
