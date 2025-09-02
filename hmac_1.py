
import hashlib
import hmac

BLOCK_SIZE = 64
SHA1_DIGEST_SIZE = 20

def hmac_sha1(key, message):
    if len(key) > BLOCK_SIZE:
        key = hashlib.sha1(key).digest()
    print(key)
    for i in key:
        print(hex(i), end=" ")
    if len(key) < BLOCK_SIZE:
        key = key + b'\x00' * (BLOCK_SIZE - len(key))
    print("adjusted key:", key)
    print("\n")
    ipad = bytes([0x36] * BLOCK_SIZE)
    opad = bytes([0x5c] * BLOCK_SIZE)

    inner_key = bytearray(BLOCK_SIZE)
    outer_key = bytearray(BLOCK_SIZE)
    for i in range(len(key)):
        inner_key[i] = key[i] ^ ipad[i]
        outer_key[i] = key[i] ^ opad[i]

    print(inner_key)
    for i in inner_key:
        print(hex(i), end=" ")
    print("\n")
    print(outer_key)
    inner_hash = hashlib.sha1(inner_key + message).digest()
    print("inner hash")
    print(inner_hash)

    hmac_result = hashlib.sha1(outer_key + inner_hash).digest()

    return hmac_result

message = b"Bonjour"
key = b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

hmac_result = hmac_sha1(key, message)
print("\n")
print("HMAC-SHA1:", hmac_result.hex())

hmac_result = hmac.new(key, message, hashlib.sha1)

print("\n")
print("HMAC-SHA1:", hmac_result.hexdigest())
print("================================================================================\n")