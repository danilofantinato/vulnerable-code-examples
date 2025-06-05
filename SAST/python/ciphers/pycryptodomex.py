from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

# Use AES with a key size of 256 bits
key = get_random_bytes(32)
cipher = AES.new(key, AES.MODE_GCM)

# Proper key management and secure key storage practices should be followed