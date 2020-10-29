alphabet="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
encrypt= input("Enter message:")
key = int(input("Enter a key number(1-25):"))
encrypt= encrypt.lower()
encrypted = ""
for letter in encrypt:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet:
        encrypted = encrypted + alphabet[newPosition]
    else:
        encrypted = encrypt + letter
    print("Your message is :", encrypted, )