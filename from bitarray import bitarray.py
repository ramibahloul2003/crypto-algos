
from bitarray import bitarray 
import numpy as np
def gf2_multiply(a, b):
    """
    Multiply two numbers in GF(2^4) and reduce modulo x^4 + x + 1 (0b10011)
    """
    result = 0
    modulus = 0b10011  # x^4 + x + 1
    
    for i in range(4):  
        if (b >> i) & 1:  
            result ^= (a << i)
    
    
    for i in range(7, 3, -1):  
        if (result >> i) & 1:  
            result ^= (modulus << (i - 4))
    
    return result & 0b1111  

def s_box(number):
    if number == bitarray('0000') :
        return bitarray ('1110')
    if number ==bitarray ('0001') :
        return bitarray('0100')
    if number == bitarray('0010') :
        return bitarray('1101')    
    if number == bitarray('0011') :
        return bitarray('0001')    
    if number == bitarray('0100') :
        return bitarray('0010')    
    if number == bitarray('0101') :
        return bitarray('1111') 
    if number == bitarray('0110') :
        return bitarray('1011')       
    if number == bitarray('0111') :
        return bitarray('1000')    
    if number == bitarray('1000') :
        return bitarray('0011')    
    if number == bitarray('1001') :
        return bitarray('1010')    
    if number == bitarray('1010') :
        return bitarray('0110') 
    if number == bitarray('1011') :
        return bitarray('1100')
    if number == bitarray('1100') :
        return bitarray('0101')
    if number == bitarray('1101') :
        return bitarray('1001')
    if number == bitarray('1110') :
        return bitarray('0000')
    if number == bitarray('1111') :
        return bitarray('0111')               
    
def generate_keys(key,round):
    
    w0 = bitarray(key[0:4])  
    w1 = bitarray(key[4:8])
    w2 = bitarray(key[8:12])
    w3 = bitarray(key[12:16])

    w4 = w0 ^ s_box(w3) ^ bitarray('0001')
    w5 = w1 ^ w4
    w6 = w2 ^ w5
    w7 = w3 ^ w6

    w8 = w4 ^ s_box(w7) ^ bitarray('0010')
    w9 = w5 ^ w8
    w10 = w6 ^ w9
    w11 = w7 ^ w10

    if round ==0 :
        w = w0 + w1 + w2 + w3
    elif  round ==1 :
        w = w4 + w5 + w6 + w7
    elif round ==2 :
        w = w8 + w9 + w10 + w11
    return w
    
def Nibble_Sub(text):
    text = bitarray(text)
    text1 = s_box(text[0:4])
    text2 = s_box(text[4:8])
    text3 = s_box(text[8:12])
    text4 = s_box(text[12:16])
    texte = text1 + text2 + text3 + text4
    return texte

def shiftrow(texte):
    m=texte[4:8]
    texte[4:8] = texte[12:16]
    texte[12:16] = m
    return texte

def mix_columns(texte):

    """
    Perform MixColumns transformation in GF(2^4)
    """
    texte_string = texte.to01()  
    
    state = np.array([
        [int(texte_string[0:4], 2), int(texte_string[8:12], 2)],
        [int(texte_string[4:8], 2), int(texte_string[12:16], 2)]
    ])
    
    mix_matrix = np.array([
        [2, 3],
        [3, 2]
    ])
    
    result_matrix = np.zeros((2, 2), dtype=int)
    for i in range(2):
        for j in range(2):
            result_matrix[i][j] = gf2_multiply(mix_matrix[i][0], state[0][j]) ^ gf2_multiply(mix_matrix[i][1], state[1][j])
    
    result_bits = bitarray(f"{result_matrix[0][0]:04b}{result_matrix[1][0]:04b}{result_matrix[0][1]:04b}{result_matrix[1][1]:04b}")
    
    return result_bits

def mini_AES(plaintexte,key) :
    
    key0 = generate_keys(key, 0)
    key1 = generate_keys(key, 1)
    key2 = generate_keys(key, 2)
    
    print("key2 :",key2)
    print("key1 :",key1)
    print("key0 :",key0)
    bit_plain = bitarray(plaintexte)^ key0
    print("first xor :",bit_plain)

    p_new = Nibble_Sub(bit_plain)
    print("Nibble_Sub:", p_new)


    shift_new = shiftrow(p_new)
    print("ShiftRow:", shift_new)


    result = mix_columns(shift_new)


    w0, w1, w2, w3 = result[0:4], result[4:8], result[8:12], result[12:16]
    result_new = w0 + w2 + w1 + w3  
    print("MixColumns:", result_new)

   
    result_final = result_new ^ key2
    phase2 = result_new ^ key1
    print("XOR with Key1:", phase2)


    phase2_new = Nibble_Sub(phase2)
    print("Nibble_Sub:", phase2_new)


    last = shiftrow(phase2_new)
    print("ShiftRow:", last)


    ciphertext = last ^ key2
    print("Ciphertext:", ciphertext)

    return ciphertext 

plaintexte = "1001110001100011"
key = "1100001111110000"

mini_AES(plaintexte,key)

def inverse_s_box(number):
    inv_sbox = {
        '0000': '1110', '0001': '0011', '0010': '0100', '0011': '1000',
        '0100': '0001', '0101': '1100', '0110': '1010', '0111': '1111',
        '1000': '0111', '1001': '1101', '1010': '1001', '1011': '0110',
        '1100': '1011', '1101': '0010', '1110': '0000', '1111': '0101'
    }
    return bitarray(inv_sbox[number.to01()])

def inverse_Nibble_Sub(text):
    text1 = inverse_s_box(text[0:4])
    text2 = inverse_s_box(text[4:8])
    text3 = inverse_s_box(text[8:12])
    text4 = inverse_s_box(text[12:16])
    return text1 + text2 + text3 + text4

def inverse_shiftrow(texte):
    m = texte[4:8]
    texte[4:8] = texte[12:16]
    texte[12:16] = m
    return texte

def inverse_gf2_multiply(a, b):
    inv_table = {2: 9, 3: 11}
    return gf2_multiply(inv_table[a], b)

def inverse_mix_columns(texte):
    texte_string = texte.to01()
    
    state = np.array([
        [int(texte_string[0:4], 2), int(texte_string[8:12], 2)],
        [int(texte_string[4:8], 2), int(texte_string[12:16], 2)]
    ])
    
    inv_mix_matrix = np.array([
        [9, 11],
        [11, 9]
    ])
    
    result_matrix = np.zeros((2, 2), dtype=int)
    for i in range(2):
        for j in range(2):
            result_matrix[i][j] = inverse_gf2_multiply(inv_mix_matrix[i][0], state[0][j]) ^ inverse_gf2_multiply(inv_mix_matrix[i][1], state[1][j])
    
    return bitarray(f"{result_matrix[0][0]:04b}{result_matrix[1][0]:04b}{result_matrix[0][1]:04b}{result_matrix[1][1]:04b}")

def mini_AES_decrypt(ciphertext, key):
    key0 = generate_keys(key, 0)
    key1 = generate_keys(key, 1)
    key2 = generate_keys(key, 2)
    
    print("Key2:", key2)
    print("Key1:", key1)
    print("Key0:", key0)
    
    phase1 = ciphertext ^ key2
    print("XOR with Key2:", phase1)
    
    phase2 = inverse_shiftrow(phase1)
    print("Inverse ShiftRow:", phase2)
    
    phase3 = inverse_Nibble_Sub(phase2)
    print("Inverse Nibble Sub:", phase3)
    
    phase4 = phase3 ^ key1
    print("XOR with Key1:", phase4)
    
    phase5 = inverse_mix_columns(phase4)
    print("Inverse MixColumns:", phase5)
    
    phase6 = inverse_shiftrow(phase5)
    print("Inverse ShiftRow:", phase6)
    
    phase7 = inverse_Nibble_Sub(phase6)
    print("Inverse Nibble Sub:", phase7)
    
    plaintext = phase7 ^ key0
    print("Final XOR with Key0 (Recovered Plaintext):", plaintext)
    
    return plaintext

ciphertext = mini_AES("1001110001100011", "1100001111110000")
decrypted_text = mini_AES_decrypt(ciphertext, "1100001111110000")
