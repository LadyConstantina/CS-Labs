# Laboratory Work Nr. 2
### Course: Cryptography & Security
### Author: Gîlca Constantina

----

## Topic: Modern Symetric Cyphers
&ensp;&ensp;&ensp; Cryptography is the study of secure communications techniques that allow only the sender and intended recipient of a message to view its contents. The term is derived from the Greek word kryptos, which means hidden. It is closely associated with encryption, which is the act of scrambling ordinary text into what's known as ciphertext and then back again upon arrival.

## Objectives
* To implement, with the scope of better understanding the terms and the domain of cryptography, the following cyphers:    
--- Rabbit stream cipher      
--- Blowfish block cipher     
* To implement the theory knowledge gathered in the course lessons, in practice.

## Technical Specifications
&ensp;&ensp;&ensp; The laboratory work was implemented in Python v3.9.2. Each type of cypher is implemented in a different class. You can test the implementations by following the next steps:    
- Open the main.impy file in a python compatible editor (make sure all the files are in the same directory upon downloading)      
- Run the code     
- Select the method of encryption by typing one of the following keys:      
&ensp;&ensp; ``` 1 ``` - Rabbit Cipher     
&ensp;&ensp; ``` 2 ``` - Blowfish Cipher     
- Provide a message you want to be encrypted     
- The encrypted message will appear as an output. You will be asked if you want to decrypt this message. Type ```y``` (YES) or ```n``` (NO).     

&ensp;&ensp;&ensp; For a better experience, please read and respect the technical specifications before trying to run the program:     
- The cyphers were implemented only for decimal digits [0-9]. Do not use any other symbols.     
- The cyphers are programmed to understand only all-numbers messages. Do not use letters or any symbols, nor spaces.     
       
&ensp;&ensp;&ensp; If you want to test the code, access the file testcode.impy in a python compatible editor.              
&ensp;&ensp;&ensp; In the following chapters, you can find more details regarding the implementation of each type of cipher.

## Rabbit Cipher
&ensp;&ensp;&ensp; Rabbit is a synchronous stream cipher that was first presented at the Fast Software Encryption workshop in 2003. It has 3 major components:     
1. The plain text that needs to be encrypted.     
2. The secret key     
3. The IV     

In order to make the process clear, please consult the cipher documentation here:      https://www.ecrypt.eu.org/stream/p3ciphers/rabbit/rabbit_p3.pdf

Using these components, the cypher follows the steps for generating the Stream:     
1. Setting the state and the counter variables by the formulas (1) and (2) from *chapter 2.2, page 4.*     
2. Calling 4 times the following set of functions:     
-- **Next State function**, applying the formulas (5) and (6) from *chapter 2.4, page 5*     
-- **Counter System function**, applying the formulas (7) and (8) from *chapter 2.5, page 6*    
3. Reinitialising the counters by the formula (3) from *chapter 2.2, page 4.*     
4. Modifying the counters by the IV by applying the formula (4) from *chapter 2.3, page 4*     
5. Repeating Step 2     
6. Extracting the Stream by applying the formula (10) from *chapter 2.6, page 6*     

Once the Stream is generated, the encryption takes place as follows:   
   
***EncryptedText[i] = PlainText[i] XOR Stream[i]***   
   
Regarding the decryption algorithm, I will leave you with the fun of discovering it. Enjoy!

## Blowfish Cipher
&ensp;&ensp;&ensp;Blowfish, A new secret-key block cipher, is proposed. It is a Feistel network, iterating a simple encryption function 16 times. It has 4 major components:    
1. The plain text that needs to be encrypted.   
2. The secret key   
3. The 18 subkeys   
4. The 4 Substitution Boxes, each with 256 entries   

In order to make the process clear, please consult the cipher documentation here:     
https://www.schneier.com/academic/archives/1994/09/description_of_a_new.html    

&ensp;&ensp;&ensp; Using these components, the cipher follows the steps:    
1. Generating the Subkeys and the Substitution Boxes    
2. Dividing the Key into a Left and Right part    
3. Iterating 16 times the following set of functions:    
-- XOR the Left part with Subkey[i]    
-- XOR the Right part with the function F of Left part    
***function F*** does the following:    
- Part the Left part into 4 equal parts, a,b,c and d.    
- Get the S[1] with the entrance a    
- Get the S[2] with the entrance b    
- Add them    
- Get S[3] with the entrance c    
- XOR it with the result of the previous addition    
- Get S[4] with entrance d    
- Add it with the result of the previous XOR    
- Return the result    
-- Swap Left and Right between them    
4. Undo the last swap    
5. XOR the Right part with the subkey 17     
6. XOR the Left part with the subkey 18     
7. Recombine the parts and get the encrypted message     

Regarding the decryption algorithm, I will leave you with the fun of discovering it. Enjoy!
## Conclusions
&ensp;&ensp;&ensp; Modern ciphers are much more complicated than classical ciphers. As they are meant to be calculated by fast computers, it is very hard, almost impossible to hack by hand. Moreover, the high number of bit-operations and their complex nature make it harder, almost impossible, for strangers to hack.

