import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
class AESCipher(object):

    def __init__(self, key, interactions=1000):
        self.bs = AES.block_size
        self.key = key
        self.interactions = interactions
    def encrypt(self, raw):
        raw = self._pad(raw)
        nbytes = [0x49, 0x76, 0x61, 0x6e, 0x20, 0x4d, 0x65, 0x64, 0x76,
                  0x65, 0x64, 0x65, 0x76]
        salt = bytes(nbytes)
        keyiv = PBKDF2(self.key, salt, 48, self.interactions)
        key = keyiv[:32]
        iv = keyiv[32:48]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        enc = base64.b64encode(iv + cipher.encrypt(raw.encode('utf-16le')))
        return self._base64_url_safe(str(enc, "utf-8"))
    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * \
            chr(self.bs - len(s) % self.bs)
    def _base64_url_safe(self, s):
        return s.replace('+', '-').replace('/', '_').replace('=', '')
    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]
enc = AESCipher("teste123")
dec = enc.encrypt("leonardo")
print(dec)
