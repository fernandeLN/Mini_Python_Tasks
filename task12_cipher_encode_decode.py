"""
Implement the keyword encoding and decoding for the Latin alphabet.
The keyword cipher uses a keyword to rearrange the letters in the alphabet.
You should add the provided keyword at the beginning of the alphabet.
A keyword is used as the key, which determines the letter matchings of the cipher alphabet to the plain alphabet.
The repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C, etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.

**Encryption:**

*The keyword is "Crypto"*

* A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
* C R Y P T O A B D E F G H I J K L M N Q S U V W X Z



**Example:**
```python
>> cipher = Cipher("crypto")
>> cipher.encode("Hello world")
"Btggj vjmgp"

>> cipher.decode("Fjedhc dn atidsn")
"Kojima is genius"
```
"""
import string


class Cipher:
    def __init__(self, key: str):
        key = key.lower()

        list_key = []
        for char in key:
            if char.isalpha():
                list_key.append(char)

        # Now the coded alphabet
        plain_alphabet = list(string.ascii_lowercase)
        coded_alphabet = list_key[:]
        for char in plain_alphabet:
            if char not in list_key:
                coded_alphabet.append(char)

        # Then the mapping of both alphabets
        self.encode_map = {}
        for i in range(len(plain_alphabet)):
            self.encode_map[plain_alphabet[i]] = coded_alphabet[i]

        self.decode_map = {}
        for i in range(len(coded_alphabet)):
            self.decode_map[coded_alphabet[i]] = plain_alphabet[i]



    def encode(self, data):
        #TODO: please add your code here
        result = []
        for char in data:
            if char.islower():
                result.append(self.encode_map.get(char))
            elif char.isupper():
                returned_to_lower = self.encode_map.get(char.lower())
                result.append(returned_to_lower.upper())
            else:
                result.append(char)
        return ''.join(result)

    def decode(self, data):
        #TODO: please add your code here
        result = []
        for char in data:
            if char.islower():
                result.append(self.decode_map.get(char))
            elif char.isupper():
                returned_to_lower = self.decode_map.get(char.lower())
                result.append(returned_to_lower.upper())
            else:
                result.append(char)
        return ''.join(result)

if __name__ == '__main__':
    cipher = Cipher("crypto")
    print(cipher.encode("Hello world"))

    print(cipher.decode("Fjedhc dn atidsn"))
