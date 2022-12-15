import random

class Cipher:

    def Encrypt(self):
        pass

    def Decrypt(self):
        pass


class Participant:
    def getPublicKey(self):
        pass

class Sender(Participant):
    def __init__(self):
        self.PublicKey = 313
        self.PrivateKey = 571

    def getPublicKey(self):
        return self.PublicKey

    def PartialKey(self,key):
        self.mod = key
        return pow(self.PublicKey,self.PrivateKey,self.mod)

    def SecretKey(self):
        self.SecretK = pow(self.PartialK,self.PrivateKey,self.mod)

    def Send(self,key):
        self.PartialK = key
        return

    def SendCipher(self,message):
        return



class Receiver(Participant):
    def __init__(self):
        self.PublicKey = 953
        self.PrivateKey = 857

    def getPublicKey(self):
        return self.PublicKey

    def PartialKey(self,key):
        return pow(self.PublicKey,self.PrivateKey,key)

    def SecretKey(self):
        self.SecretK = pow(self.PartialK,self.PrivateKey,self.mod)

    def Send(self,key):
        self.PartialK = key
        return

    def ReceiveCipher(self,message):
        return

class DiffieHallman(Cipher):
    def __init__(self,plaintext,decrypt_bool):
        self.Sender = Sender()
        self.Receiver = Receiver()
        self.Key = self.setSecretKey()
        self.PlainText = plaintext
        if self.Key :
            self.Communication()
        else:
            print("Couldn't define secret key!")


    def setSecretKey(self):

        PublicKeyReceiver = Receiver.getPublicKey()
        PartialKeySender = Sender.PartialKey(PublicKeyReceiver)
        Sender.Send(PartialKeySender)

        PublicKeySender = Sender.getPublicKey()
        PartialKeyReceiver = Receiver.PartialKey(PublicKeySender)
        Receiver.Send(PartialKeyReceiver)

        SecretKey1 = Sender.SecretK
        SecretKey2 = Receiver.SecretK

        if SecretKey1 == SecretKey2 :
            return SecretKey1
        else:
            return 0

    def Communication(self):

        self.encrypted_message = self.Encrypt()
        print("Encrypted message: \n",self.encrypted_message)
        Sender.SendCipher(self.encrypted_message)
        Receiver.ReceiveCipher(self.encrypted_message)
        self.decrypted_message = self.Decrypt()
        print("Decrypted message: \n",self.decrypted_message)

        return

    def Encrypt(self):
        encrypted_text = ""
        for character in self.PlainText:
            encrypted_text += chr(ord(character)+self.Key)
        return encrypted_text

    def Decrypt(self):
        decrypted_text = ""
        for character in self.encrypted_message:
            decrypted_text += chr(ord(character)-self.Key)
        return decrypted_text
    

