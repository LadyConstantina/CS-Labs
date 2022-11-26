from argon2 import PasswordHasher
from Crypto.Util.number import *

class Participants:
    
    def set_PublicKey(self):
        pass
    
    def set_PrivateKey(self):
        pass
    
    def get_PublicKey(self):
        pass

#+===========================================================================================

class Sender(Participants):
    
    def __init__(self):
        self.set_PublicKey()
        self.set_PrivateKey()
    
    def set_PublicKey(self):
        # For RSA we need 2 prime numbers
        prime1 = 1051446937579387829
        prime2 = 696907085081608369
        # N is a public key = prime1 * prime2
        self.N = 732760820386434997658767113743140901
        # E is a public key that
        # does not share a factor
        # with (prime1-1)*(prime2-1)
        self.E = 65537
        
    def set_PrivateKey(self):
        # The Private Key is
        # the inverse of E 
        # mod (prime1-1)*(prime2-1) 
        self.PrivateK = 575356501766415283802339857698644801
    
    def get_PublicKey(self):
        return self.N,self.E 
    
    def Encode_message(self,string):
        return string.encode('utf-8')
    
    def Encrypt_message(self,plaintext):
        #String to bytes
        message = self.Encode_message(plaintext)
        #Bytes to long integer
        message = bytes_to_long(message)
        #Encrypted message = Message ^ Private Key mod N
        encrypted_message = pow(message,self.PrivateK,self.N)
        return str(encrypted_message)
    
    def Send_message(self,plaintext):
        #Encrypted message as a string
        enc_message = self.Encrypt_message(plaintext)
        #Hashing the plaintext
        ph = PasswordHasher()
        h = ph.hash(plaintext)
        #The final message is EncryptedPlaintext.Hash
        return enc_message+"."+h

#+================================================================================================================

class Receiver(Participants):
    
    def set_PublicKey(self):
        return "None needed"
        
    def set_PrivateKey(self):
        return "None needed"
    
    def get_PublicKey(self):
        return "None needed"
    
    def Check_message(self,message,received_hash):
        ph = PasswordHasher()
        
        #Verifying if the message hashed is equal to the hash received
        if ph.verify(received_hash,message):
            print("Message accepted!")
            return True
        else:
            print("Message denied!")
            return False
        
    def Decrypt_message(self,message,Public_key,N):
        #Splitting the message received to encrypted plaintext and hash
        strings = message.split(".")
        encrypted_message = int(strings[0])
        h = strings[1]
        
        #Decrypted Message = Encrypted Message ^ Public Key mod N
        decrypted_message = pow(encrypted_message,Public_key,N)
        #Long integer to bytes
        decrypted_message = long_to_bytes(decrypted_message)
        #Bytes to plaintext
        plaintext = decrypted_message.decode('utf-8')
        
        #Checking if the hash of the decoded message is the same with the hash received
        if self.Check_message(plaintext,h):
            print("Message received:   "+plaintext)

#+=======================================================================================================================

class Communication:
    
    def __init__(self):
        #2 participants: Sender and Receiver
        #Step 1: Generate the private and public keys
        self.Sender = Sender()
        self.Receiver = Receiver()
        
        #Step 2: Generate the message
        message = self.Generate_Message()
        
        #Step 3: Send the message
        print(self.Send_Message(message))
        
        #Step 4: Receiver gets the message and computes it
        self.Received_Message(message)
        
        print("End of communication session!")
        
    def Generate_Message(self):
        #Step 1: Get the text as an input
        Plaintext = input("What is the text you want to send?")
        #Step 2: The sender encrypts the message before sending
        Message = self.Sender.Send_message(Plaintext)
        print("Message genereated!")
        return Message
    
    def Send_Message(self,message):
        print("Sending message ...")
        return "Message delivered succesfully!"
        
    def Received_Message(self,message):
        #Receiver requests the public key and N from the sender
        N, PublicKey = self.Sender.get_PublicKey()
        #Receiver computes the decryption of the message
        self.Receiver.Decrypt_message(message,PublicKey,N)

#+========================================================================================================================

def main():
    start = Communication()