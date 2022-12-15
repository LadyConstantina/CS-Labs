from argon2 import PasswordHasher
from Crypto.Util.number import *


class Participants:
    
    def set_PublicKey(self):
        pass
    
    def set_PrivateKey(self):
        pass
    
    def get_PublicKey(self):
        pass

class Sender(Participants):
    
    def __init__(self):
        self.set_PublicKey()
        self.set_PrivateKey()
    
    def set_PublicKey(self):
        prime1 = 5058733
        prime2 = 913873
        self.N = 4623039502909
        self.E = 12345678901232456975
        
    def set_PrivateKey(self):
        self.PrivateK = 2770368766703
    
    def get_PublicKey(self):
        return self.N,self.E 
    
    def Encode_message(self,string):
        return string.encode('utf-8')
    
    def Encrypt_message(self,plaintext):
        message = self.Encode_message(plaintext)
        message = bytes_to_long(message)
        encrypted_message = pow(message,self.PrivateK,self.N)
        return str(encrypted_message)
    
    def Send_message(self,plaintext):
        enc_message = self.Encrypt_message(plaintext)
        ph = PasswordHasher()
        h = ph.hash(plaintext)
        return enc_message+"."+h

class Receiver(Participants):
    
    def set_PublicKey(self):
        return "None needed"
        
    def set_PrivateKey(self):
        return "None needed"
    
    def get_PublicKey(self):
        return "None needed"
    
    def Check_message(self,message,received_hash):
        ph = PasswordHasher()
        if ph.verify(received_hash,message):
            return True
        else:
            return False
        
    def Decrypt_message(self,message,Public_key,N):
        strings = message.split(".")
        encrypted_message = int(strings[0])
        h = strings[1]
        decrypted_message = pow(encrypted_message,Public_key,N)
        decrypted_message = long_to_bytes(decrypted_message)
        plaintext = decrypted_message.decode('utf-8')
        if self.Check_message(plaintext,h):
            print("Message received:   "+plaintext)

class Communication:
    
    def __init__(self,plaintext,decrypt_bool):
        self.Sender = Sender()
        self.Receiver = Receiver()
        self.Plaintext = plaintext
        message = self.Generate_Message()
        print(self.Send_Message(message))
        self.Received_Message(message)
        
    def Generate_Message(self):
        Message = self.Sender.Send_message(self.Plaintext)
        return Message
    
    def Send_Message(self,message):
        return
        
    def Received_Message(self,message):
        N, PublicKey = self.Sender.get_PublicKey()
        self.Receiver.Decrypt_message(message,PublicKey,N)