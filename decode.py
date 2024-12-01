#!/usr/bin/python3

import base64
import hashlib

# [INTRO.01] Exercise: Base64 encoding 

str1 = "VGhpcyBpcyB0b28gZWFzeQ=="

str2 = "VWtkc2EwbEliSFprVTBKdVdsaFJaMlJIYUhCamVVSjVZVmRrYjJSRU9EMD0="

print(base64.b64decode(str1))

decoded1_str2 = base64.b64decode(str2)

decoded2_str2 = base64.b64decode(decoded1_str2)

print(base64.b64decode(decoded2_str2))

#openSSL cert:
cert = """MIIFSTCCBDGgAwIBAgISAwNxVcbr7SlT+h/xX11IWMsaMA0GCSqGSIb3DQEBCwUA
MDIxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQswCQYDVQQD
EwJSMzAeFw0yMzAyMDkxMzExMTVaFw0yMzA1MTAxMzExMTRaMBUxEzARBgNVBAMT
Cnd3dy5rZWEuZGswggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDB5+iw
RPfSPkRYncsUz7JsO0m9h/5fYq4pyFRAHRy9IQ0EJEJwfL9DUwH2QxL/Ac3n3cVo
LqLoiIZqXzkJ3E43gMg9Z8VU/CmDapJelNV1XDwzPcK0PZLYNizmfkix/T/9VPkb
idTkOOFtne+z4Z44sna2+KFct0U+a9Xb3/ggLnknIlal1qlCBTZlpncSs35uLMZi
jT/Sq0a194jwUGIlJDJW0Hjxh9ZDAwcvbvlQmDbL2sqnCLIQaS9kbQdVovrBTlaf
kvXVSLc1a95lfB7X//1o1c13bct/FQt3qZf3dm1cvPuhk4s52q+UgxBtrDntdcFC
nJA+9DHPGifww9LPAgMBAAGjggJ0MIICcDAOBgNVHQ8BAf8EBAMCBaAwHQYDVR0l
BBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYE
FNTo1KoWz8u0Fav0tq0riTEILrFrMB8GA1UdIwQYMBaAFBQusxe3WFbLrlAJQOYf
r52LFMLGMFUGCCsGAQUFBwEBBEkwRzAhBggrBgEFBQcwAYYVaHR0cDovL3IzLm8u
bGVuY3Iub3JnMCIGCCsGAQUFBzAChhZodHRwOi8vcjMuaS5sZW5jci5vcmcvMEUG
A1UdEQQ+MDyCDWNwYW5lbC5rZWEuZGuCC2lwdjYua2VhLmRrggZrZWEuZGuCCndo
bS5rZWEuZGuCCnd3dy5rZWEuZGswTAYDVR0gBEUwQzAIBgZngQwBAgEwNwYLKwYB
BAGC3xMBAQEwKDAmBggrBgEFBQcCARYaaHR0cDovL2Nwcy5sZXRzZW5jcnlwdC5v
cmcwggEDBgorBgEEAdZ5AgQCBIH0BIHxAO8AdQB6MoxU2LcttiDqOOBSHumEFnAy
E4VNO9IrwTpXo1LrUgAAAYY2hCbxAAAEAwBGMEQCIGaInBhEzPupXu0bvxZmV7+3
lNfnE2GnNv8JWsR7Q8qZAiAS5YruKLDKypuNrdQycnGBGz6iuvf0Io35VaOpOIrA
1gB2AK33vvp8/xDIi509nB4+GGq0Zyldz7EMJMqFhjTr3IKKAAABhjaEJs0AAAQD
AEcwRQIhALse7ZakkON5fqPMXoaLfLXYiY2bIKWcLKdpawConHh1AiBT/71BPfkz
hN8atJU2jNJSKH8hfTCMpLSgIFup/BA37TANBgkqhkiG9w0BAQsFAAOCAQEACSIN
vWkZk8xDBwBL0wZlkO7VCMbCD4mQxFD5DxLj6ZeFzNuFBf1/CBPQl/CKhXZk5m8B
7QcgxhaDtr/lAnne/glfkv/AjrqtkeGgI49mrLbGuHq1HKnM+bqyxV7wO8SkzJ6T
UjjoAZ0g7VpOMoo01oM0chOdJCTMkYiok42ZgYh/iys44zjSQrJ/Rpcuf6vR6ZoD
9oslG++EReNksIZFDg5+KLWxekgBaafYxprpZG8bolkztsgkLoUcPRuWPlDLE4mp
XFtpRcL+5UBv4lmuhSITh+NwImuOj40t7yJMmIoOdgrvOkcmdfVkvE2aDIn6rN9i
WvX3t39/mvq3zvewdA=="""

print(base64.b64decode(cert))
# denne giver bare den rå version af certifikatet, det er ikke som kommandoen:
# openssl x509 -noout -text -in test.cert
# som viser det i human-readable format


# [INTRO.02] Exercise: Password Hashing

# password giver hash: f9e75553669606c10ce89621ffa4ce5c

# er hashet med en simpel hashing algoritme der giver plain text hexademical såsom md5 og sha1 og SHA-256
# det er ikke god beskyttelse, de kan brute forces og der kan bruges rainbow tables
# det er en md5 hash fordi den er på 32 karakter hexadecimal (16 byte) mens SHA-1 er på 40 og SHA-256 er på 64
# 32 karakter hexadecimal er 16 byte fordi hver hex er en halv byte

# det er mere sikkert at bruge algoritmer såsom bcrypt, scrypt, og Argon2
# brug salt så at samme password ikke giver ens hash
# brug pepper 

# ved at gøre disse ting er passworded dog stadig bare plaintext hexadecimal
# i stedet kunne passworded encodes med base64 fx eller gemmes som json som indeholder metadata 
# algoritmen og saltet brugt 


# [INTRO.03] Exercise: Password Hashing - hard mode!

# hint: usr/share/   wordlist    john the ripper 

# hashen: 762ff3fda60a5663e96ae208bf4b56f54b9d74e954147350193b59f16806b3fa
# er 64-character hexadecimal som er 64/2=32 bytes, som er 256 bits. SHA-256 er brugt

# crack password:
# hashcat og john the ripper
# methoder der kan bruges: brute-force, mask attack, dict attack, rainbow table

# john --format=raw-sha256 --wordlist=rockyou.txt hash.txt

# hashcat gør det samme:

# hashcat -a 0 -m 1400 hash.txt rockyou.txt  

# husk: hashcat skal kun have hashen i en fil mens john skal have user:<hash>

# john kan åbenbart også kun køre cracking kommandoen én gang da den så cacher det og siger: 
# crackede passwords gemmes dog i: ~/.john/john.pot

#cat ~/.john/john.pot
# viser:
# $SHA256$762ff3fda60a5663e96ae208bf4b56f54b9d74e954147350193b59f16806b3fa:Sebastian123



#  2. time crypto fra slides Applied Crypto_2_Hashing.pptx

# bruger hashlib library: https://docs.python.org/3/library/hashlib.html

# cyberchef: https://gchq.github.io/CyberChef/
# massere af crypto tools 

# bits of digests of algorithms:
# md5: 128
# sha1: 160
# sha256: 256

# exercise løsning: md5 for recommend.ps og order.ps giver ens hash/digest, 
# # viser at md5 ikke er særlig sikker, det er birtgday attack, collission 


with open("recommend.ps", 'rb') as file:
        recommend = file.read()

with open("order.ps", 'rb') as file:
        order = file.read()

print(hashlib.algorithms_available)

print(hashlib.md5(recommend).hexdigest())
print(hashlib.md5(order).hexdigest())
# the digest gotten from md5sum in the terminal:
print("a25f7f0b29ee0b3968c860738533a4b9")

# sha-1 for de samme filer:
# sha1sum ~/Downloads/recommend.ps
# sha-2
# shasum -a 256 ~/Downloads/order.ps
# de giver forskellig hash