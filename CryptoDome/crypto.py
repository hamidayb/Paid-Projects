from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib
import hmac
import binascii, os


BLOCK_SIZE = 32

print("-------------------------------- TASK 01 ------------------------------------")

print("\nAES-ECB mode:\n")

fptr = open("pt1.txt","w")
fptr.write("This is text message 1")
fptr.close()
fptr = open("pt2.txt","w")
fptr.write("This is text message 1")
fptr.close()

key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_ECB)
f1data = pad(open("pt1.txt").read().encode(),BLOCK_SIZE)
encrypted_1_text = base64.b64encode(cipher.encrypt(f1data))

cipher = AES.new(key, AES.MODE_ECB)
f2data = pad(open("pt2.txt").read().encode(),BLOCK_SIZE)
encrypted_2_text = base64.b64encode(cipher.encrypt(f2data))


fout = open("ct1.txt","wb")
fout.write(encrypted_1_text)
fout.close()

fout = open("ct2.txt","wb")
fout.write(encrypted_2_text)
fout.close()

ct1 = open("ct1.txt","rb")
ct2 = open("ct2.txt","rb")

print("ct1.txt :  ",ct1.read().decode())
print("ct2.txt :  ",ct2.read().decode())

print("-------------------------------- TASK 02 ------------------------------------")

print("\nAES-CBC mode:\n")

iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CBC,iv)

f1data = open("pt1.txt").read()
f2data = open("pt2.txt").read()

encrypted_1_text = base64.b64encode(iv + cipher.encrypt(pad(f1data.encode('utf-8'),AES.block_size)))
encrypted_2_text = base64.b64encode(iv + cipher.encrypt(pad(f2data.encode('utf-8'),AES.block_size)))

fout = open("ct1.txt","wb")
fout.write(encrypted_1_text)
fout.close()

fout = open("ct2.txt","wb")
fout.write(encrypted_2_text)
fout.close()

ct1 = open("ct1.txt")
ct2 = open("ct2.txt")

print("ct1.txt :  "+ct1.read())
print("ct2.txt :  "+ct2.read())

print("-------------------------------- TASK 03 ------------------------------------")

print("\nHMAC Authentication:\n")

k1 = get_random_bytes(32)
f1data = open("pt1.txt").read().encode()
myhmac = hmac.new(f1data, k1, hashlib.md5)

fout = open("tag1.txt","wb")
fout.write(base64.b64encode(myhmac.digest()))

f1d = open("pt1.txt","w")
f1d.write("This is the test message 2")
f1d.close()

f1data = open("pt1.txt").read().encode()
myhmac = hmac.new(f1data, k1, hashlib.md5)

fout = open("tag2.txt","wb")
fout.write(base64.b64encode(myhmac.digest()))
fout.close()

tag1 = open("tag1.txt").read()
tag2 = open("tag2.txt").read()

print("tag1.txt :  "+tag1)
print("tag2.txt :  "+tag2)

print("-------------------------------- TASK 04 ------------------------------------")

print("\nAES-GCM-256 mode:\n")

def encrypt_AES_GCM(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(encryptedMsg, secretKey):
    (ciphertext, nonce, authTag) = encryptedMsg
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext

k2 = os.urandom(32)  # 256-bit random encryption key

msg = open("pt1.txt").read()
print("Text before encryption:  "+msg)

msg = msg.encode()
encryptedMsg, nounce, tag = encrypt_AES_GCM(msg, k2)

ct3 = open("ct3.txt","wb")
ct3.write(encryptedMsg)
ct3.close()

ct = open("ct3.txt","rb").read()
decryptedMsg = decrypt_AES_GCM((ct,nounce,tag), k2)

print("Cipher after decryption: "+decryptedMsg.decode())
