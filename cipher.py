# Define the alphabet and key
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789öäüÖÄÜ!?,;.:()[]{}+-*/=<>_@#$%^&|~`"\'\\ '
key = 'X9Y2Z7W1V8U3T6S4R5Q0P'
shuffledAlphabet = 'mn8op2qrs3tuvwxyz9R0STUVWXYZabcdef4ghijkl7ABCDEFGHIJKLMN1OP5Q6öäüÖÄÜ!?,;.:()[]{}+-*/=<>_@#$%^&|~`"\'\\ '

# Caesar shift function
def caesarShift(str, shift):
    return ''.join([alphabet[(alphabet.index(char) + shift + len(alphabet)) % len(alphabet)] if char in alphabet else char for char in str])
    #explanation: alphabet.index(char) gets the index of the character in the alphabet
    #alphabet[(alphabet.index(char) + shift + len(alphabet)) % len(alphabet)] shifts the character by the shift value
    #if the character is not in the alphabet it is left as it is

# XOR Encrypt function
def xorEncrypt(str, key):
    return ''.join([chr(ord(char) ^ ord(key[i % len(key)])) for i, char in enumerate(str)])
    #explanation: ord(char) gets the ASCII value of the character
    #ord(key[i % len(key)]) gets the ASCII value of the key character
    #chr(ord(char) ^ ord(key[i % len(key)]) XORs the ASCII values of the character and the key character
    #enumerate(str) returns the index and the character of the string
    #i % len(key) makes sure that the key is repeated if the string is longer than the key

# Reverse string function
def reverseString(str):
    return str[::-1]
    #explanation: str[::-1] reverses the string

# Substitution cipher function
def substitutionCipher(str, sourceAlphabet, targetAlphabet):
    return ''.join([targetAlphabet[sourceAlphabet.index(char)] if char in sourceAlphabet else char for char in str])
    #explanation: sourceAlphabet.index(char) gets the index of the character in the sourceAlphabet
    #targetAlphabet[sourceAlphabet.index(char)] gets the character at the index in the targetAlphabet
    #if the character is not in the sourceAlphabet it is left as it is

# Cipher function
def cipher(text):
    cipherText = text
    cipherText = substitutionCipher(cipherText, alphabet, shuffledAlphabet)
    #to file
    file = open("substitution.txt", "w")
    file.write(cipherText)
    cipherText = caesarShift(cipherText, 13)
    file = open("caesar.txt", "w")
    file.write(cipherText)
    cipherText = xorEncrypt(cipherText, key)
    file = open("xor.txt", "w")
    file.write(cipherText)
    cipherText = reverseString(cipherText)
    print(cipherText)
    return cipherText
    #explanation: the text is first substituted with the shuffledAlphabet
    #then it is shifted by 13
    #then it is XOR encrypted with the key
    #then it is reversed

# Decipher function
def decipher(text):
    decipherText = text
    decipherText = reverseString(decipherText)
    decipherText = xorEncrypt(decipherText, key)
    decipherText = caesarShift(decipherText, -13)
    decipherText = substitutionCipher(decipherText, shuffledAlphabet, alphabet)
    return decipherText
    #explanation: the text is first reversed
    #then it is XOR decrypted with the key
    #then it is shifted by -13
    #then it is substituted with the alphabet


# Define the text to be ciphered
text = "The highest bidding price is 406714 NZ$"

# Cipher the text
cipherText = cipher(text)
print(cipherText)

# Decipher the text
decipherText = decipher(cipherText)
print("Deciphered text: ", decipherText)
#export the ciphered text to a file
file = open("ciphered.txt", "w")
file.write(cipherText)
file.close()
#export the deciphered text to a file
file = open("deciphered.txt", "w")
file.write(decipherText)
file.close()
