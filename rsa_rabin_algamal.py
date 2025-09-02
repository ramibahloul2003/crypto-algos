import random
from sympy import isprime, mod_inverse
from hashlib import sha256

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result


def generate_prime(bits=512):
    while True:
        p = random.getrandbits(bits)
        if isprime(p):
            return p

def generate_rsa_keys():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    d = mod_inverse(e, phi)

    return (n, e), (n, d)  

def rsa_encrypt(m, pub_key):
    n, e = pub_key
    return mod_exp(m, e, n)

def rsa_decrypt(c, priv_key):
    n, d = priv_key
    return mod_exp(c, d, n)

message = 123456789
public_key, private_key = generate_rsa_keys()

c = rsa_encrypt(message, public_key)
m = rsa_decrypt(c, private_key)

print(f"message: {message}")
print(f"chiffré: {c}")
print(f"déchiffré: {m}")

print("================================================================================\n")

def sign_message(message, private_key):
    hash_value = int(sha256(message.encode()).hexdigest(), 16)
    return rsa_encrypt(hash_value, private_key)

def verify_signature(message, signature, public_key):
    hash_value = int(sha256(message.encode()).hexdigest(), 16)
    return hash_value == rsa_decrypt(signature, public_key)


def generate_rabin_keys(bits=512):
    p, q = generate_prime(bits), generate_prime(bits)
    while p % 4 != 3:
        p = generate_prime(bits)
    while q % 4 != 3:
        q = generate_prime(bits)
    n = p * q
    return (n,), (p, q)

def rabin_encrypt(m, public_key):
    n, = public_key
    return pow(m, 2, n)

def rabin_decrypt(c, private_key):
    p, q = private_key
    n = p * q
    mp = pow(c, (p + 1) // 4, p)
    mq = pow(c, (q + 1) // 4, q)
    return mp, -mp % p, mq, -mq % q

def generate_elgamal_keys(bits=512):
    p = generate_prime(bits)
    g = random.randint(2, p - 1)
    x = random.randint(2, p - 2)
    y = pow(g, x, p)
    return (p, g, y), (p, x)

def elgamal_encrypt(m, public_key):
    p, g, y = public_key
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p
    return c1, c2

def elgamal_decrypt(c1, c2, private_key):
    p, x = private_key
    s = pow(c1, x, p)
    m = (c2 * mod_inverse(s, p)) % p
    return m

if __name__ == "__main__":
    # RSA
    rsa_pub, rsa_priv = generate_rsa_keys()
    message = 12345
    cipher = rsa_encrypt(message, rsa_pub)
    print
    print("RSA Decryption:", rsa_decrypt(cipher, rsa_priv))
    
    # RSA Signature
    signature = sign_message("Hello", rsa_priv)
    print("Signature Valid:", verify_signature("Hello", signature, rsa_pub))
    
    # Rabin
    rabin_pub, rabin_priv = generate_rabin_keys()
    rabin_cipher = rabin_encrypt(message, rabin_pub)
    print("Rabin Encryption:", rabin_cipher)
    print("Rabin Decryption Candidates:", rabin_decrypt(rabin_cipher, rabin_priv))
    
    # ElGamal
    elgamal_pub, elgamal_priv = generate_elgamal_keys()
    c1, c2 = elgamal_encrypt(message, elgamal_pub)
    print("ElGamal Encryption:", c1, c2)
    print("ElGamal Decryption:", elgamal_decrypt(c1, c2, elgamal_priv))