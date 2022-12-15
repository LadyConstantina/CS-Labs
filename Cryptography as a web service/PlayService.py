from classicciphers import CeasarClassic,CeasarRandom,Vigenere,Playfair
from symmetricciphers import Rabbit,Blowfish
from asymmetricciphers import DiffieHallman
from digitalsignature import Communication


class Play:
    def __init__(self,type_subscription) -> None:
        if type_subscription == "Basic":
            PlayBasic()
        else:
            PlayPremium()
        

class PlayBasic:
    def __init__(self) -> None:
        self.SelectCipher()
    
    def SelectCipher(self):
        print('''Let's Play!
        What cipher would you like to use?

        1 - Classic Ceasar Cipher
        2 - Random Alphabet Ceasar Cipher
        3 - Vigenere Cipher
        4 - Playfair Cipher

        99 - to exit
        ''')

        i = int(input("Type a number from 1 to 4: "))

        if i == 99:
            print("Bye!")
            return

        print("What is the plaintext you want to play with?")
        plaintext = input()

        print("Would you want to decrypt the message as well?(y/n)")
        decryption = input()
        if decryption == "y":
            decryption = True
        else:
            decryption = False

        if i == 1:
            CeasarClassic(plaintext,decryption)
            self.EndGame()
        elif i == 2:
            CeasarRandom(plaintext,decryption)
            self.EndGame()
        elif i == 3:
            Vigenere(plaintext,decryption)
            self.EndGame()
        elif i == 4:
            Playfair(plaintext,decryption)
            self.EndGame()
        else:
            print("Error: not correct number typed in!")
            self.SelectCipher()

    def EndGame(self):
        again = input("It was fun! Wanna try again? (y/n): ")
        if again == "y":
            self.SelectCipher()
        else:
            print("Bye!")    

class PlayPremium:

    def __init__(self) -> None:
        self.SelectCipher()

    def SelectCipher(self):
        print('''Let's Play!
        What would you like to play with?
        1 - Classic Ciphers (ex: Caeser, Vigenere, Playfair)
        2 - Symmetric Ciphers (ex: Blowfish,Rabbit)
        3 - Asymmetric Ciphers (Diffie-Halman)
        4 - Digital Signatures

        10 - if you want to quit
        ''')
        i = int(input("Type here from 1 to 4: "))
        if i == 10:
            print("Bye!")
            return
        print("What is the plaintext you want to play with?")
        plaintext = input()
        if i == 1:
            self.Classic(plaintext)
        elif i == 2:
            self.Symmetric(plaintext)
        elif i == 3:
            self.Assymetric(plaintext)
        elif i == 4:
            self.DigitalS(plaintext)
        else:
            print("Wrong number! Let's try again!")
            self.SelectCipher()
    
    def Classic(self,plaintext):
        print("Would you want to decrypt the message as well?(y/n)")
        decryption = input()
        if decryption == "y":
            decryption = True
        else:
            decryption = False
        
        print('''What cipher would you like to use?
        1 - Classic Ceasar Cipher
        2 - Random Alphabet Ceasar Cipher
        3 - Vigenere Cipher
        4 - Playfair Cipher
        ''')
        i = int(input("Type a number from 1 to 4: "))
        if i == 1:
            CeasarClassic(plaintext,decryption)
            self.EndGame()
        elif i == 2:
            CeasarRandom(plaintext,decryption)
            self.EndGame()
        elif i == 3:
            Vigenere(plaintext,decryption)
            self.EndGame()
        elif i == 4:
            Playfair(plaintext,decryption)
            self.EndGame()
        else:
            print("Error: not correct number typed in!")
            self.EndGame()
    
    def Symmetric(self,plaintext):
        print("Would you want to decrypt the message as well?(y/n)")
        decryption = input()
        if decryption == "y":
            decryption = True
        else:
            decryption = False
        
        print('''What cipher would you like to use?
        1 - Blowfish Cipher
        2 - Rabbit Cipher
        ''')
        i = int(input("Type a number from 1 to 2: "))
        if i == 1:
            Blowfish(plaintext,decryption)
            self.EndGame()
        elif i == 2:
            Rabbit(plaintext,decryption)
            self.EndGame()
        else:
            print("Error: not correct number typed in!")
            self.EndGame()
    
    def Assymetric(self,plaintext):
        print("Would you want to decrypt the message as well?(y/n)")
        decryption = input()
        if decryption == "y":
            decryption = True
        else:
            decryption = False

        DiffieHallman(plaintext,decryption)
        self.EndGame()
    
    def DigitalS(self,plaintext):
        Communication(plaintext,decrypt_bool=True)
        self.EndGame()
    
    def EndGame(self):
        again = input("It was fun! Wanna try again? (y/n): ")
        if again == "y":
            self.SelectCipher()
        else:
            print("Bye!")





    