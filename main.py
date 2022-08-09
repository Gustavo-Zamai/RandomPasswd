import string
import random

chars = list(string.ascii_letters + string.digits + string.punctuation)

def genRandomPasswd ():
  len = int(input('Enter the password length: '))
  random.shuffle(chars)
  passwd = []
  for x in range(len):
    passwd.append(random.choice(chars))
  random.shuffle(passwd)
  print("".join(passwd))

genRandomPasswd()
