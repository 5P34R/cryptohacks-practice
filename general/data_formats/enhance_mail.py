
from Crypto.Util import number
from Crypto.PublicKey import RSA

key = open("privacy_enhanced_mail.pem", 'rb').read()
value = RSA.import_key(key)
print(value.d)
  