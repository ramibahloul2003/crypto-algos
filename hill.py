import numpy as np

def check_matrix(matrix):
    det = round(np.linalg.det(matrix)) % 26
    return "good" if np.gcd(int(det), 26) == 1 else "not inversible"

def encry_hill(text, tab):
    result = ""
    text = ''.join([char for char in text.upper() if char.isalpha()])
    if len(text) % 2 != 0:
        text += 'X'

    while text:
        first, second = text[0], text[1]
        tabl = np.array([[ord(first) - ord('A')], [ord(second) - ord('A')]])
        res = np.dot(tab, tabl) % 26

        
        result += chr(int(res[0][0]) + ord('A'))
        result += chr(int(res[1][0]) + ord('A'))

        text = text[2:]

    return result

def inv(tab):
    det = (tab[0][0] * tab[1][1] - tab[0][1] * tab[1][0]) % 26

    det_inv = pow(int(det), -1, 26)
    
    tab_new = np.array([[tab[1][1], -tab[0][1]],[-tab[1][0], tab[0][0]]]) % 26

    tab_new = (tab_new * det_inv) % 26
    return tab_new.astype(int)  


key2 = np.array([[9, 4], [5, 7]])
if check_matrix(key2) == "good":

  
  print("Matrix ", key2)
  key3 = inv(key2)  
  print("Inverse Matrix", key3)

  text = encry_hill("chiffrhill", key2)
  print("chiffre:", text)


  text = encry_hill(text, key3)
  print("dechiff:", text)
else :
    print("try again")