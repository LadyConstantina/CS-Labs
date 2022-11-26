# Laboratory Work Nr. 4
### Course: Cryptography & Security
### Author: Gîlca Constantina

----

## Topic: Digital Signature       
&ensp;&ensp;&ensp; A **digital signature** is a mathematical scheme for verifying the authenticity of digital messages or documents. A valid digital signature, where the prerequisites are satisfied, gives a recipient very high confidence that the message was created by a known sender (authenticity), and that the message was not altered in transit (integrity).             
&ensp;&ensp;&ensp; For a better understanding of Digital Signature, we will implement the **RSA Assymetric encryption method** with **Argon2 Hashing method**.       
               
## Objectives       
* To implement, with the scope of better understanding the terms and the domain of cryptography, a *Digital Signature* using *RSA* for encryption and *Argon2* for hashing.       
* To implement the theory knowledge gathered in the course lessons, in practice.       
       
## Technical Specifications
&ensp;&ensp;&ensp; The laboratory work was implemented in Python v3.9.2. You can test the implementation by following the next steps:       
- Download the main.py and digitalsigniature.py files. Make sure they are in the same directory.      
- Open the command line and enter the directory where the files are located.
- Run the following line:
```python main.py```           
                                   
&ensp;&ensp;&ensp; If you want to see the code, access the file *digitalsigniature.py* in a python compatible editor and you will see the implementation. Every step is commented on carefully and an example is analysed in the following chapter.       
       
&ensp;&ensp;&ensp; The cypher is compatible with utf-8 characters. Feel free to introduce any compatible characters in the message you want to encrypt.       
&ensp;&ensp;&ensp; In the following chapter, you can find a detailed example with code snippets for a better understanding of how things work.       
       
## Digital Signature applied (using RSA)       
&ensp;&ensp;&ensp; **RSA** (**Rivest–Shamir–Adleman**) is a public-key cryptosystem that is widely used for secure data transmission. It is also one of the oldest.        
&ensp;&ensp;&ensp; The method uses the following 4 components:       
	1. 2 different prime numbers which helps in computing the public and private keys. In our example:
		```
		prime 1 = 1051446937579387829
		prime 2 = 696907085081608369
		```       
	2. A public key  *N = prime<sub>1</sub> x prime<sub>2</sub>*. In our example:
	```N = 732760820386434997658767113743140901```       
	3. A public key *E* which does not share a factor with *(prime<sub>1</sub> - 1) x (prime<sub>2</sub> - 1)*. In our example:
	```E = 65537```       
	4. A private key which is *E<sup>-1</sup> mod ((prime<sub>1</sub> - 1) x (prime<sub>2</sub> - 1))*. In our example:
	```Private Key = 575356501766415283802339857698644801```       

Using these components, the Sender follows the steps for generating and sending a message:       
1. The *Sender* receives the plaintext from the user:             
```Plaintext = input("What is the text you want to send?")```                 
2. The plaintext is encoded according to utf-8 into bytes by the function:                
	```        
	def  Encode_message(self,string):         
		return  string.encode('utf-8')         
	```        
3. Transform the bytes into a long integer.
4. Encrypt the message by applying the formula:
**Encrypted_message = Plaintext <sup>Private Key</sup> mod N**
These steps are achieved by the following function:
	```
	def  Encrypt_message(self,plaintext):
		message = self.Encode_message(plaintext)
		message = bytes_to_long(message)
		encrypted_message = pow(message,self.PrivateK,self.N)
		return  str(encrypted_message)
	```
5. Hash the plaintext. For this, I used the `argon2` library. The function responsible for the step is:
	```
	def  Send_message(self,plaintext):
		#Encrypted message as a string
		enc_message = self.Encrypt_message(plaintext)
		#Hashing the plaintext
		ph = PasswordHasher()
		h = ph.hash(plaintext)
		#The final message is EncryptedPlaintext.Hash
		return  enc_message+"."+h
	```
6. Send the message to the receiver.

Let's assume the user introduces ***"Hello World!"*** as the plaintext.                
It will be transformed into the number ***22405534230753928650781647905***.                                     
Later the number will be encrypted into ***533964879063792078988031684323000578***.                     
The hash of the plaintext will be ***4$QEAphBnBS3jhghHZ69FJwg$5E10q9tNLdG+JZ+Hyw03VsXXuArM0RKoL5jvUhv3uYQ***.      
Finally, the message send to the receiver is ***"533964879063792078988031684323000578.4\$QEAphBnBS3jhghHZ69FJwg$5E10q9tNLdG+JZ+Hyw03VsXXuArM0RKoL5jvUhv3uYQ"*** .                             
                                 
Once the message is delivered, the receiver follows these steps:       

1. Requests the public keys E and N from the Sender:
```N, PublicKey = self.Sender.get_PublicKey()```
2. Decrypts the message by the formula *Decrypted_message = Encrypted_message <sup>E</sup> mod N*
3. Encode the bytes by utf-8 and transforms them into a string.
The function responsible is:
	```
	def  Decrypt_message(self,message,Public_key,N):
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
		if  self.Check_message(plaintext,h):
		print("Message received: "+plaintext)
	```
4. Once the message is decrypted the Receiver hashes it and compares it to the hash received. If they are the same, the message is accepted. Otherwise, declined. 
This step is implemented in the function:
	```
	def  Check_message(self,message,received_hash):
		ph = PasswordHasher()
		#Verifying if the message hashed is equal to the hash received
		if  ph.verify(received_hash,message):
			print("Message accepted!")
			return  True
		else:
			print("Message denied!")
			return  False
	```                   
Now in our example, the program returns the following:
```
What is the text you want to send? 
Hello World!
Message genereated!
Sending message ...
Message delivered succesfully!
Message accepted!
Message received:   Hello World!
End of communication session!
```
## Conclusions       
&ensp;&ensp;&ensp; Digital Signature is an efficient method of assuring the authenticity and integrity of the message upon arrival to the receiver. Since hashes are practically impossible to decrypt, it ensures that the communication is strictly between the sender and receiver and any malicious activity can be intercepted and stopped before it causes any damage.      
&ensp;&ensp;&ensp; The RSA is one of the oldest Asymmetric ciphers but it's still a widely used one and very effective indeed. It was easy to implement but very hard to break when large numbers are involved, even impossible.     
&ensp;&ensp;&ensp; The final process computes fast, but it's hard to break and ensures the malicious activity can be stopped before affecting the integrity of the information. Those are the attributes we are looking for in message transmission.     

