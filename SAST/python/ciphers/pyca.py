import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

key = os.urandom(32)
iv = os.urandom(16)

aes256 = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
chacha20 = Cipher(algorithms.ChaCha20(key, iv), mode=None, backend=default_backend())