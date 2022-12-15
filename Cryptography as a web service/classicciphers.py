import random
import textwrap
from collections import OrderedDict

class Cipher:

    def Encrypt(self):
        pass

    def Decrypt(self):
        pass

class CeasarClassic(Cipher):

    def __init__(self,plaintext,decrypt_bool):
        self.Key = 5
        self.PlainText = plaintext
        self.Encrypt()
        if decrypt_bool:
            self.Decrypt()
    
    def Encrypt(self):
        self.encrypted = ""

        sentences = self.PlainText.split(".")
        if not sentences[len(sentences)-1]:
            sentences = sentences[:-1]

        words = []
        for sentence in sentences:
            words.append(sentence.split(" "))

        for sentence_set in words:
            for word in sentence_set:
                for letter in word:
                    if letter.isupper():
                        limit = 65
                    else:
                        limit = 97

                    char_num = ord(letter)-limit
                    char_num = (char_num + self.Key) % 26
                    char_num = chr(char_num + limit)
                    self.encrypted += char_num
                self.encrypted += " "
            self.encrypted = self.encrypted.rstrip()
            self.encrypted += ". "
        
        print("Encrypted message: \n",self.encrypted)
    
    def Decrypt(self):
        self.decrypted = ""

        sentences = self.encrypted.split(".")
        sentences = sentences[:-1]
        words = []
        for sentence in sentences:
            words.append(sentence.split(" "))

        for sentence_set in words:
            for word in sentence_set:
                for letter in word:
                    if letter.isupper():
                        limit = 65
                    else:
                        limit = 97

                    char_num = ord(letter) - limit
                    char_num = (char_num + (26 - self.Key)) % 26
                    char_num = chr(char_num + limit)
                    self.decrypted += char_num
                self.decrypted += " "
            self.decrypted = self.decrypted.rstrip()
            self.decrypted += ". "

        print("Decrypted message: \n",self.decrypted)    

class Vigenere(Cipher):
    def __init__(self,plaintext,decrypt_bool):
        word_key = "vigenere"
        self.Key = []
        for letter in word_key:
            self.Key.append(ord(letter)-96)
        self.PlainText = plaintext
        self.Encrypt()
        if decrypt_bool:
            self.Decrypt()

    def Encrypt(self):
        self.encrypted = ""

        sentences = self.PlainText.split(".")
        if not sentences[len(sentences)-1]:
            sentences = sentences[:-1]

        words = []
        for sentence in sentences:
            words.append(sentence.split(" "))

        key_i = 0
        for sentence_set in words:
            for word in sentence_set:
                for letter in word:
                    if letter.isupper():
                        limit = 65
                    else:
                        limit = 97

                    char_num = ord(letter) - limit
                    char_num = (char_num + self.Key[key_i]) % 26
                    key_i = (key_i + 1) % len(self.Key)
                    char_num = chr(char_num + limit)
                    self.encrypted += char_num
                self.encrypted += " "
            self.encrypted = self.encrypted.rstrip()
            self.encrypted += ". "
        
        print("Encrypted message: \n",self.encrypted)

    def Decrypt(self):
        self.decrypted = ""

        sentences = self.encrypted.split(".")
        sentences = sentences[:-1]
        words = []
        for sentence in sentences:
            words.append(sentence.split(" "))

        key_i = 0
        for sentence_set in words:
            for word in sentence_set:
                for letter in word:
                    if letter.isupper():
                        limit = 65
                    else:
                        limit = 97
                    
                    char_num = ord(letter) - limit
                    char_num = (char_num + (26 - self.Key[key_i])) % 26
                    key_i = (key_i + 1) % len(self.Key)
                    char_num = chr(char_num + limit)
                    self.decrypted += char_num
                self.decrypted += " "
            self.decrypted = self.decrypted.rstrip()
            self.decrypted += ". "
        
        print("Decrypted message: \n",self.decrypted)

class CeasarRandom(Cipher):
    def __init__(self,plaintext,decrypt_bool):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.alphabet = ''.join(random.sample(self.alphabet,26))
        self.Key = 5
        self.PlainText = plaintext
        self.Encrypt()
        if decrypt_bool:
            self.Decrypt()

    def Encrypt(self):
        self.encrypted = ""

        sentences = self.PlainText.split(".")
        if not sentences[len(sentences)-1]:
            sentences = sentences[:-1]

        words = []
        for sentence in sentences:
            words.append(sentence.split(" "))

        for sentence_set in words:
            for word in sentence_set:
                for letter in word:
                    Upper = False
                    if letter.isupper():
                        letter = letter.lower()
                        Upper = True
                    
                    char_num = self.alphabet.find(letter)
                    char_num = (char_num + self.key) % 26
                    char_num = self.alphabet[char_num]
                    if Upper:
                        char_num = char_num.upper()
                    self.encrypted += char_num
                self.encrypted += " "
            self.encrypted = self.encrypted.rstrip()
            self.encrypted += ". "
        print("Encrypted message: \n",self.encrypted)

    def Decrypt(self):
        self.decrypted = ""

        sentences = self.encrypted.split(".")
        sentences = sentences[:-1]
        words = []
        for sentence in sentences:
            words.append(sentence.split(" "))

        for sentence_set in words:
            for word in sentence_set:
                for letter in word:
                    Upper = False
                    if letter.isupper():
                        letter = letter.lower()
                        Upper = True
                        
                    char_num = self.alphabet.find(letter)
                    char_num = (char_num + (26 - self.key)) % 26
                    char_num = self.alphabet[char_num]
                    if Upper:
                        char_num = char_num.upper()
                    self.decrypted += char_num
                self.decrypted += " "
            self.decrypted = self.decrypted.rstrip()
            self.decrypted += ". "

        print("Decrypted message: \n",self.decrypted)

class Playfair(Cipher):
    def __init__(self,plaintext,decrypt_bool):
        word = "playfair"
        self.GetKey(word)
        self.PlainText = plaintext
        self.Encrypt()
        if decrypt_bool:
            self.Decrypt()
    
    def GetKey(self,word):
        word = word.upper()
        self.Key = "".join(OrderedDict.fromkeys(word))

        self.code2letter = {}
        self.letter2code = {}
        self.bogusletter = "Q"

        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if letter not in self.key:
                self.Key += letter
        
        i,j = 0,0
        for letter in self.Key:

            code = str(i)+str(j)
            j+=1
            if j == 5:
                j=0
                i+=1

            self.code2letter[code] = letter
            self.letter2code[letter] = code
    
    def Encrypt(self):
        self.encrypted = ""

        sentences = self.PlainText.split(".")
        if not sentences[len(sentences)-1]:
            sentences = sentences[:-1]

        words = []
        for sentence in sentences:
            words.append(sentence.split(" "))

        duos = []
        for sentence_set in words:
            for word in sentence_set:
                new_duo = ""
                word = word.upper()
                word = word.replace("J","I")
                for letter in word:
                    if not new_duo:
                        new_duo = new_duo + letter
                        
                    elif new_duo:
                        if letter in new_duo:
                            duos.append(new_duo)
                            new_duo = letter
                        else:
                            new_duo = new_duo + letter
                            duos.append(new_duo)
                            new_duo = ""           
                if new_duo:
                    duos.append(new_duo)
        
        encrypted_duos = []
        for i in range(len(duos)):
            if len(duos[i]) == 1:
                duos[i] = duos[i] + self.bogusletter
            
            letter_1 = duos[i][0]
            letter_2 = duos[i][1]
            code_1 = self.letter2code[letter_1]
            code_2 = self.letter2code[letter_2]
            
            if code_1[0] == code_2[0]:
                change_int_2_1 = (int(code_1[1])+1)%5
                change_int_2_2 = (int(code_2[1])+1)%5
                code_1 = code_1[0] + str(change_int_2_1)
                code_2 = code_2[0] + str(change_int_2_2)
                encrypted_duo = self.code2letter[code_1] + self.code2letter[code_2]
            
            elif code_1[1] == code_2[1]:
                change_int_1_1 = (int(code_1[0])+1)%5
                change_int_1_2 = (int(code_2[0])+1)%5
                code_1 = str(change_int_1_1) + code_1[1]
                code_2 = str(change_int_1_2) + code_2[1]
                encrypted_duo = self.code2letter[code_1] + self.code2letter[code_2]
            
            else:
                change_int_2_1 = int(code_2[1])
                change_int_2_2 = int(code_1[1])
                code_1 = code_1[0] + str(change_int_2_1)
                code_2 = code_2[0] + str(change_int_2_2)
                encrypted_duo = self.code2letter[code_1] + self.code2letter[code_2]
                
            encrypted_duos.append(encrypted_duo)
        
        for duo in encrypted_duos:
            self.encrypted += duo
        print("Encrypted message: \n",self.encrypted)

    def Decrypt(self):
        self.decrypted= ""
        
        duos = []
        duos += textwrap.wrap(self.encrypted,2)
        
        decrypted_duos = []
        for i in range(len(duos)):
            
            decrypted_duo = ""
            letter_1 = duos[i][0]
            letter_2 = duos[i][1]
            code_1 = self.letter2code[letter_1]
            code_2 = self.letter2code[letter_2]
            
            if code_1[0] == code_2[0]:
                change_int_2_1 = abs((int(code_1[1])-1))
                change_int_2_2 = abs((int(code_2[1])-1))
                code_1 = code_1[0] + str(change_int_2_1)
                code_2 = code_2[0] + str(change_int_2_2)
                decrypted_duo = self.code2letter[code_1] + self.code2letter[code_2]
                
            elif code_1[1] == code_2[1]:
                change_int_1_1 = abs((int(code_1[0])-1))
                change_int_1_2 = abs((int(code_2[0])-1))
                code_1 = str(change_int_1_1) + code_1[1]
                code_2 = str(change_int_1_2) + code_2[1]
                decrypted_duo = self.code2letter[code_1] + self.code2letter[code_2]
                
            else:
                change_int_2_1 = int(code_2[1])
                change_int_2_2 = int(code_1[1])
                code_1 = code_1[0] + str(change_int_2_1)
                code_2 = code_2[0] + str(change_int_2_2)
                decrypted_duo = self.code2letter[code_1] + self.code2letter[code_2]
                
            decrypted_duos.append(decrypted_duo)
            
        for duo in decrypted_duos:
            self.decrypted += duo
            
        self.decrypted =  self.decrypted.replace(self.bogusletter,"")
        print("Decrypted message: \n",self.decrypted)


