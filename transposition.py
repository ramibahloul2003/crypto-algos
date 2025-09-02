import numpy as np # type: ignore



def insert_string(text):
    
    table = np.full((5,5), ' ', dtype=str)
    text = text.replace(" ", "")
    
    char_list = list(text)
 
    index = 0  
    for row in range(5):  
        for col in range(5):  
            if index < len(char_list):  
                table[row, col] = char_list[index]  
                index += 1  
            else:
                break  

    return table



def transposition(tab):
     texte =""
     for col in range (5) :
        for row in range (5):
           if tab[row][col] != ' ': 
             texte += tab[row][col]
            
     return texte



def transform(matrix):
    rows, cols = len(matrix), len(matrix[0])
    
    transformed = np.full((cols, rows), ' ', dtype=str)
   
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != ' ':
                transformed[j][i] = matrix[i][j]
    
    return transformed


text = "TUER LE ROI DEMAIN A MINUIT"


table = insert_string(text)
print(table)
texte2=(transposition(table))

print("chiffre :"  ,texte2)
print(transform(table))


text=text.replace(" ","")
print("dechiff :" ,text)
