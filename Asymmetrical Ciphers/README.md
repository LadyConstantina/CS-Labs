# Laboratory Work Nr. 3
### Course: Cryptography & Security
### Author: Gîlca Constantina

----

## Topic: Asymmetric Cryptography       
&ensp;&ensp;&ensp; Asymmetric Cryptography, also known as Public Key Cryptography, is the field of cryptographic systems that uses pairs of related keys to encrypt a message. Simply put, both the sender and the user have a pair of keys, one public and one secret. Using these pairs they can exchange partial keys which computed will generate to both users the same secret key but can not be retrieved by any third party.     
&ensp;&ensp;&ensp; For a better understanding of Asymmetric Cryptography, we will implement the **Diffie-Hellman encryption method**.       
## Objectives       
* To implement, with the scope of better understanding the terms and the domain of cryptography, the Diffie-Hellman encryption method.       
* To implement the theory knowledge gathered in the course lessons, in practice.       
       
## Technical Specifications
&ensp;&ensp;&ensp; The laboratory work was implemented in Python v3.9.2. You can test the implementation by following the next steps:       
- Open the main.impy file in a python compatible editor (make sure all the files are in the same directory upon downloading)       
- Run the code       
             
&ensp;&ensp;&ensp; If you want to test the code, access the file testcode.ipynb in a python compatible editor and you will see the implementation. Every step is commented on carefully and an example is analysed in the following chapter.       
       
&ensp;&ensp;&ensp; The cypher is compatible with any ASCII characters. Feel free to introduce any characters in the message you want to encrypt.       
&ensp;&ensp;&ensp; In the following chapter, you can find a detailed example with code snippets for a better understanding of how things work.       
       
## Diffie-Hellman encryption       
&ensp;&ensp;&ensp; *Diffie–Hellman key exchange* is a method of securely exchanging cryptographic keys over a public channel and was one of the first public-key protocols as conceived by Ralph Merkle and named after Whitfield Diffie and Martin Hellman. DH is one of the earliest practical examples of public key exchange implemented within the field of cryptography. Published in 1976 by Diffie and Hellman, this is the earliest publicly known work that proposed the idea of a private key and a corresponding public key.           
&ensp;&ensp;&ensp; The method uses the following 4 components:       
1. The Sender's public key       
2. The Receiver's public key       
3. The Sender's private key       
4. The Receiver's private key       
       
Using these components, the cypher follows the steps for generating the Secret Key:       
1. The *Sender* of the message should set a public and a private key. In our case, as the user of the code, you will perform the sender's actions. Therefore you will be asked to introduce a public key and a private key.       
***The responsible functions for this step:***       
```       
def set_PublicKey(self):       
        public_key = int(input("Type in your public key:"))       
        return public_key       
               
def set_PrivateKey(self):       
        private_key = int(input("Set your secret key: "))       
        return private_key       
```       
       
Assume we run the program and introduce **29** as our *public key* and **11** as our *private key*.       
       
2. The Receiver's public and private keys are set by the program.       
***The responsible functions for this step:***       
```       
def get_PublicKeyReceiver(self):       
        public_key = 33       
        return public_key       
       
def get_PrivateKeyReceiver(self):       
        private_key = 13       
        return private_key       
```       
The program sets those values to **33** as *Receiver's Public Key and* **13** as *Receiver's Private Key*.       
       
3. With this data we need to set the secret Key, so we call the following function:       
```       
def Set_SecretKey(self):       
               
        self.partialKey = self.Power(self.PublicKey1, self.PrivateKey1, self.PublicKey2)       
               
        #Assume we are sending this partial key to the receiver       
               
        #As a response we get the receivers partial key       
        self.partialKey_received = self.get_PartialKey()       
               
        Secret_Key = self.Power(self.partialKey_received, self.PrivateKey1, self.PublicKey2)       
               
        return Secret_Key       
```       
**1:**  The function sets the Sender's (Your's) partial Key. The formula for the partial key is the following:       
       
Key<sub>partial</sub> = **PublicKey**<sub>sender</sub><sup>PrivateKey<sub>sender</sub></sup> mod **PublicKey**<sub>receiver</sub>       
       
In our case:       
PublicKey<sub>sender</sub> is our public key = **29**,        
PrivateKey<sub>sender</sub> is our private key = **11** ,       
PublicKey<sub>receiver</sub> is set by the program = **33**.        
       
Applying the formula, we get:       
       
Key<sub>partial</sub> = 29 <sup>11</sup> mod 33 = ***29***       
       
In the program, this formula is applied by the **Power** function:       
```       
def Power(self, number, power, modulo):       
        result = 1       
        while power:       
            result *= number       
            result = result % modulo       
            power -=1       
        return result       
```       
       
*Little trick:       
This function calculates the power of the number one by one and each time computes the modulo. **Why this way?**       
When dealing with big numbers at big powers we can get results that are greater than the maximal integer possible. However, in the end, we still need to perform a mod operation which will limit this big number to one smaller than the modulo number.
Hence, to avoid the maximal integer problem, we perform the mod operation after each power operation. The result still remains the same.*       
       
This Key is sent then to the receiver.       
       
**2:** the function gets the Receiver's partial key. It is computed by the program in the following function:       
```       
def get_PartialKeyfromReceiver(self):       
        partial_key = self.Power(self.PublicKey1, self.PrivateKey2, self.PublicKey2)       
        return partial_key       
```       
       
It applies the following formula:       
Key<sub>partial</sub> = **PublicKey**<sub>sender</sub><sup>PrivateKey<sub>receiver</sub></sup> mod **PublicKey**<sub>receiver</sub>       
       
In our case:       
PublicKey<sub>sender</sub> is our public key = **29**,        
PrivateKey<sub>receiver</sub> is set by the program = **13** ,       
PublicKey<sub>receiver</sub> is set by the program = **33**.        
       
Applying the formula in the same **Power** function, we get:       
       
Key<sub>partial</sub> = 29 <sup>13</sup> mod 33 = ***2***       
       
This partial Key is received by the Sender (You).       
       
**3:** Having the Receiver's partial Key we can compute the Secret Key by the following formula:       
Key<sub>secret</sub> = **Partial Key**<sub>receiver</sub><sup>PrivateKey<sub>sender</sub></sup> mod **PublicKey**<sub>receiver</sub>       
       
In our case:       
PartialKey<sub>receiver</sub> is the key we got from the receiver = **2**,        
PrivateKey<sub>sender</sub> is our private key = **11** ,       
PublicKey<sub>receiver</sub> is set by the program = **33**.       
       
Applying the formula in the same **Power** function, we get:       
       
Key<sub>secret</sub> = 2 <sup>11</sup> mod 33 = ***2***        
       
Now we got the secret key = **2** !       
       
4. Now that we have the secret key we can encrypt a message.       
The plain text for encryption is retrieved from the user by the function:       
```       
def get_PlainText(self):       
        message = str(input("Write down the message you want to send: "))       
        return message       
```       
Let's assume when we are asked to introduce the message we want, we type in:       
```       
Cryptography is fun!       
```       
The encryption process is performed by the **Encryption** function:       
```       
def Encryption(self):       
        self.Encrypted_text = ""       
        for character in self.PlainText:       
            self.Encrypted_text += chr(ord(character)+self.SecretKey)       
```       
       
The process is simple, we take every character from the text and transform it into their order number from ASCII table, add the Secret Key number - **2** and transform the new number into ASCII character:       
C -> 67 + 2 -> 69 -> E       
r -> 114 + 2 -> 116 -> t       
y -> 121 + 2 -> 123 -> {       
...       
! -> 33 + 2 -> 35 -> #       
       
As a result, we get the encrypted message:       
```       
Et{rvqitcrj{"ku"hwp#       
```       
5. After we have encrypted the message, the algorithm enters the **Decryption** function:       
```       
    def Decryption(self):       
        confirmation = str(input("Do you want to decrypt the message (as a receiver)? (y/n)"))       
        if confirmation == "n":       
            return       
               
        Secret_Key = self.Power(self.partialKey, self.PrivateKey2, self.PublicKey2)       
               
        self.Decrypted_text = ""       
        for character in self.Encrypted_text:       
            self.Decrypted_text += chr(ord(character)-Secret_Key)       
```              
**1:** You are first asked if you do want to decrypt the message from the Receiver's perspective. Type ``y`` for yes and ``n`` for no.       
**2:** In order to decrypt the message, the Receiver has to compute the secret key. Do you remember when you sent your partial key to him? It was the number **29**. Now he's got to apply the formula:       
       
Key<sub>secret</sub> = **Partial Key**<sub>sender</sub><sup>PrivateKey<sub>receiver</sub></sup> mod **PublicKey**<sub>receiver</sub>       
       
In our case:       
PartialKey<sub>sender</sub> is the key you sent = **29**,        
PrivateKey<sub>receiver</sub> is set by the program = **13** ,       
PublicKey<sub>receiver</sub> is set by the program = **33**.       
       
Applying the formula in the same **Power** function, we get:       
       
Key<sub>secret</sub> = 29 <sup>13</sup> mod 33 = ***2***        
       
*Explanation:       
We ended up with the same key. **Why this happened?**       
From the start we got 2 public keys, let's name them **S** and **R**.
And we got 2 private keys, let's name them **a** and **b**.       
What we did to compute the secret key from the sender's perspective is:       
**(S<sup>b</sup> mod R)<sup>a</sup> mod R = S<sup>ba</sup> mod R**       
What we did to compute the secret key from the receiver's perspective is:       
**(S<sup>a</sup> mod R)<sup>b</sup> mod R = S<sup>ab</sup> mod R**       
As we can see, in the end, we performed the same computations, just in a different order. Hence we got the same secret key.*       
       
**3:** Now we got to decrypt the message. The process is the same, but this time we subtract the secret key number:       
E -> 69 - 2 -> 67 -> C       
t -> 116 - 2 -> 114 -> r       
{ -> 123 - 2 -> 121 -> y       
...       
\# -> 35 - 2 -> 33 -> !       
       
As a result, we get the plain text:       
```       
Cryptography is fun!       
```            
         
The output of the program in this session is the following:    
```    
Type in your public key:29    
Set your secret key: 11    
    
Sender (You):    
Public Key = 29    
Private Key = 11   
Partial Key = 29    
Secret Key = 2    
    
Receiver:    
Public Key = 33    
Private Key = 13     
Partial Key = 2    
Secret Key = 2    
    
Write down the message you want to send: Cryptography is fun!    
The plain text: Cryptography is fun!    
Encrypted: Et{rvqitcrj{"ku"hwp#    
Do you want to decrypt the message? (y/n)y    
The encrypted text: Et{rvqitcrj{"ku"hwp#    
Decrypted: Cryptography is fun!    
```    
## Conclusions       
&ensp;&ensp;&ensp; Asymmetric cyphers are a little bit easier to compute and they keep the level of security the symmetric cyphers do. Moreover, they are personalised to each individual case of the sender-receiver.       
&ensp;&ensp;&ensp; The Diffie-Hellman encryption definitely revolutionised modern cryptography, starting a new era. Nowadays, this encryption method is used in message encryptions, Password Authenticated Agreement and even in Forward secrecy-based protocols that for each session generates a new pair of public keys and discard them once the session is finished.       
&ensp;&ensp;&ensp; However, the Diffie-Hellman method can be cracked if either the generated public numbers are not truly random or by man-in-the-middle attack, hence the implementation should prevent those threats.       

