import os
import base64
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

class DESCipher:
    def __init__(self, key):
        self.key = key
        self.cipher = DES.new(key, DES.MODE_ECB)

    def encrypt(self, plaintext):
        plaintext_padded = pad(plaintext.encode(), DES.block_size)
        ciphertext = self.cipher.encrypt(plaintext_padded)
        return ciphertext

    def decrypt(self, ciphertext):
        decipher = DES.new(self.key, DES.MODE_ECB)
        decrypted_text = decipher.decrypt(ciphertext)
        decrypted_text_unpadded = decipher.decrypt(ciphertext)[:-decipher.block_size]
        return decrypted_text_unpadded.decode()

# Generate a random 8-byte key
key = os.urandom(8)

# Create a cipher instance
cipher = DESCipher(key)

# Convert string to byte array
plaintext = 'Jesame C. Sawan-on'

# Encryption
ciphertext = cipher.encrypt(plaintext)
ciphertext_base64 = base64.b64encode(ciphertext)
print("Ciphertext: ", ciphertext_base64)

# Decryption
decrypted_text = cipher.decrypt(ciphertext)
print("Decrypted text: ", decrypted_text)