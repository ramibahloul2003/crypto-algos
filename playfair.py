import string


def formule_text(text):    
    
    text = text.lower().replace(" ", "")  
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            result += "x"  
        if i + 1 < len(text):
            result += text[i + 1]    
        i += 2

    if len(result) % 2 != 0:
        result += "x"  

    return result


def create_matrix(key):
    
    key = key.lower() 
    matrix_list = list(dict.fromkeys(key))  
    alphabet = "abcdefghiklmnopqrstuvwxyz"  

    for char in alphabet:  
        if char not in matrix_list:
            matrix_list.append(char)

    return [matrix_list[i:i + 5] for i in range(0, 25, 5)]


def find_position(matrix, letter):
    
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None


def playfair_encrypt(text, matrix):
    
    text = formule_text(text)  
    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:  
            result += matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]

        elif col_a == col_b:  
            result += matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]

        else:  
            result += matrix[row_a][col_b] + matrix[row_b][col_a]
        print (text[i],text[i+1])
        
    return result


def playfair_dycrypt(text, matrix):
    
    text = formule_text(text)  
    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:  
            result += matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]

        elif col_a == col_b:  
            result += matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]

        else:  
            result += matrix[row_a][col_b] + matrix[row_b][col_a]

    return result


key = "playfair"
message = "PLAYFAIR EXAMPLE"    

matrix = create_matrix(key)
print("Playfair Matrix:")
for row in matrix:
    print(" ".join(row))

print("chiffre:",  playfair_encrypt(message, matrix ))