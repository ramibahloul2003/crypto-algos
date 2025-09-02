import string


def position(x):
    alphabet = list(string.ascii_lowercase)  # Liste des lettres de a à z
    x = x.lower()  
    if x in alphabet:
        return alphabet.index(x) 
    else:
        return -1

def decalage(x, n):
    alphabet = string.ascii_lowercase 
    x = x.lower()  
    positionX = position(x)

    if positionX >= 0:
        newPositionX = (positionX + n) % 26  
        return alphabet[newPositionX]
    else:
        return x

def codage_substitution(texte, substitution):
    
    alphabet = string.ascii_lowercase  # Alphabet standard a-z
    texte = texte.lower()  # Convertir en minuscules pour correspondre à l'alphabet
    newTexte = ""
    
    for char in texte.lower():
       
        if char in ["é","è"]:
            char ="e"
        elif char == "à":
            char = "a"
        elif char == "ç":
            char = "c"
        elif char not in alphabet:
            char = ""          
        newTexte += char
    
    resultat = ""
    lenTexte = len(newTexte)
    lenSubstitution = len(substitution)
    finalSubstitution = ""
    
    for i in range (0,lenTexte):
        
        if i == lenSubstitution:
            substitution = substitution + substitution
            lenSubstitution = lenSubstitution + lenSubstitution
        
        finalSubstitution += substitution.lower()[i]
        
    for i in range (0,lenTexte):
        
        resultat += decalage(newTexte[i],position(finalSubstitution[i]))
        
    return resultat

print("message code :",codage_substitution("le c#hiffrement!","azerty"))

def decodage_substitution(texte, substitution):
    
    alphabet = string.ascii_lowercase  # Alphabet standard a-z
    texte = texte.lower()  # Convertir en minuscules pour correspondre à l'alphabet
    newTexte = ""
    
    for char in texte.lower():
        
        if char in ["é","è"]:
            char ="e"
        elif char == "à":
            char = "a"
        elif char == "ç":
            char = "c"
        elif char not in alphabet:
            char = ""          
        newTexte += char
        
    
    resultat = ""
    lenTexte = len(newTexte)
    lenSubstitution = len(substitution)
    finalSubstitution = ""
    
    for i in range (0,lenTexte):
        
        if i == lenSubstitution:
            substitution = substitution + substitution
            lenSubstitution = lenSubstitution + lenSubstitution
        
        finalSubstitution += substitution.lower()[i]
        
    for i in range (0,lenTexte):
        
        resultat += decalage(newTexte[i],-position(finalSubstitution[i]))
        
    return resultat

print("message decode :" ,decodage_substitution("ldgybdfqidxlt","azerty"))