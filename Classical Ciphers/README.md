# Laboratory Work Nr. 1
### Course: Cryptography & Security
### Author: Gîlca Constantina

----

## Topic: Classical Ciphers
&ensp;&ensp;&ensp;Cryptography is the study of secure communications techniques that allow only the sender and intended recipient of a message to view its contents. The term is derived from the Greek word kryptos, which means hidden. It is closely associated to encryption, which is the act of scrambling ordinary text into what's known as ciphertext and then back again upon arrival.

## Objectives
* To implement, with the scope of better understanding the terms and the domain of cryptography, the following ciphers:
- Caesar cipher variant 1
- Caesar cipher variant 2
- Vigenere cipher
- Playfair cipher
* To implement the theory knowledge gathered in the course lessons, in practice.

## Implementation
&ensp;&ensp;&ensp;The laboratory work was implemented in Python v3.9.2. Each type of the cipher is implemented in a different class. You can test the implementations by following the next steps:
- Open the main.impy file in a python compatible editor (make sure all the files are in the same directory upon downloading)
- Run the code
- Provide a message you want to be encrypted
- Select the method of encryption by typing one of the following keywords:
&ensp;&ensp; -- ``` 1 ``` - Caesar cipher variant 1
&ensp;&ensp; -- ``` 2 ``` - Caesar cipher variant 2
&ensp;&ensp; -- ``` 3 ``` - Vigenere cipher
&ensp;&ensp; -- ``` 4 ``` - Playfair cipher
- The encrypted message will be apear as an output. You will be asked if you want to decrypt this message. Type y (YES) or n (NO).

&ensp;&ensp;&ensp; For a better experience, please read and respect the technical specifications before trying to run the program:
- The ciphers were implemented only for the English alphabet. Do not use any other languages's symbols.
- The ciphers are programmed to understand only all-characters messages. Do not use numbers or any characters, other than ``` . ? ! ``` and upper or lower letters.

&ensp;&ensp;&ensp; In the following chapters you can find more details regarding the implementation of each type of cipher.
