from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# AES-256 in GCM mode
key = b'ThisIsAVeryLongKeyForAES256Cipher'
iv = b'ThisIsAVeryLongIV'

cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(b"This is a secret message") + encryptor.finalize()

# ChaCha20-Poly1305
key = b'ThisIsAVeryLongKeyForChaCha20Poly1305'
iv = b'ThisIsAVeryLongIV'

cipher = Cipher(algorithms.ChaCha20(key, iv), mode=None, backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(b"This is a secret message") + encryptor.finalize()

# Authenticated encryption should be used whenever possible
# to protect against chosen-ciphertext attacks and other vulnerabilities.