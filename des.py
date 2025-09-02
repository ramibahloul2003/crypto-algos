import numpy as np



P10 = [3,5,2,7,4,10,1,9,8,6]
P8 = [6,3,7,4,8,5,10,9]
IP = [2,6,3,1,4,8,5,7]
Inv_IP = [4,1,3,5,7,2,8,6]
EP = [4,1,2,3,2,3,4,1]
P4 = [2,4,3,1]
K = "1010000010"
P = "01110010"

S0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 0, 2]]

S1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]

#########################################################################

def permute(k, P):
  
    return "".join(k[i - 1] for i in P)  

############################################################################

def split_and_left_shift(bits, shift=1):

    mid = len(bits) // 2
    left, right = bits[:mid], bits[mid:]
    left_shifted = left[shift:] + left[:shift]  
    right_shifted = right[shift:] + right[:shift]  
    return left_shifted + right_shifted

#############################################################################

def xor_bits(a, b):

    return "".join(str(int(x) ^ int(y)) for x, y in zip(a, b))

##############################################################################

def split_bits(bits):

    mid = len(bits) // 2
    return bits[:mid], bits[mid:]

##############################################################################

def s_box_substitution(bits, s_box):

    row = int(bits[0] + bits[3], 2) 
    col = int(bits[1] + bits[2], 2)  
    return format(s_box[row][col], '02b')  

##############################################################################

def swap(bits):
    L,R = split_bits(bits)
    return R + L

################################ key generator function ##############################################

def key_generation(key):
    
    P10_permutaion = permute(key,P10)
    first_shift = split_and_left_shift(P10_permutaion,1)
    K1 = permute(first_shift,P8)
    second_shift = split_and_left_shift(first_shift,2)
    K2 = permute(second_shift,P8)
    
    return K1,K2


################################ fk function ##############################################

def fk(bits,key):
    L,R = split_bits(bits)
    print("L and R :",L," ",R)
    EP_permutation = permute(R,EP)
    print("EP permutation :",EP_permutation)
    first_xor = xor_bits(EP_permutation,key)
    print("first xor :",first_xor)
    s0,s1 = split_bits(first_xor)
    print("s0 and s1 :",s0," ",s1)
    S0_result = s_box_substitution(s0,S0)
    print("S0 result :",S0_result)
    S1_result = s_box_substitution(s1,S1)
    print("S1 result :",S1_result)
    P4_permutation = permute(S0_result + S1_result , P4)
    print("P4 permutation :",P4_permutation)
    second_xor = xor_bits(L,P4_permutation)
    print("second xor :",second_xor)
    
    return second_xor + R


##################################### ENCRYPTION ##############################################

def encryption(plainText,key):
    K1,K2 = key_generation(key)
    print("K1 and K2 :",K1," ",K2)
    IP_permutaion = permute(plainText,IP)
    print("IP permutation :",IP_permutaion)
    fk_result = fk(IP_permutaion,K1)
    print("fk result :",fk_result)
    swap_result = swap(fk_result)
    print("swap result :",swap_result)
    second_fk_result = fk(swap_result,K2)
    print("second fk result :",second_fk_result)
    cypherText = permute(second_fk_result,Inv_IP)
    print("the cypher text is :",cypherText)
    
    return cypherText
    
     
encryption(P,K)

######################################### DECRYPTION #################################################

def decryption(cypherText,key):
    K1,K2 = key_generation(key)
    IP_permutaion = permute(cypherText,IP)
    fk_result = fk(IP_permutaion,K2)
    swap_result = swap(fk_result)
    second_fk_result = fk(swap_result,K1)
    plainText = permute(second_fk_result,Inv_IP)
    
    print("plain Text :",plainText)
    
    return plainText
    
    
decryption(encryption(P,K),K)