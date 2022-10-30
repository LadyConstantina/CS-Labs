# Laboratory Work Nr. 1
### Course: Cryptography & Security
### Author: Gîlca Constantina

----

## Topic: Classical Cyphers
&ensp;&ensp;&ensp; Cryptography is the study of secure communications techniques that allow only the sender and intended recipient of a message to view its contents. The term is derived from the Greek word kryptos, which means hidden. It is closely associated with encryption, which is the act of scrambling ordinary text into what's known as ciphertext and then back again upon arrival.

## Objectives
* To implement, with the scope of better understanding the terms and the domain of cryptography, the following cyphers:   
-- Caesar cypher variant 1   
-- Caesar cypher variant 2   
-- Vigenere cypher   
-- Playfair cypher   
* To implement the theory knowledge gathered in the course lessons, in practice.

## Technical Specifications
&ensp;&ensp;&ensp; The laboratory work was implemented in Python v3.9.2. Each type of cypher is implemented in a different class. You can test the implementations by following the next steps:
- Open the main.ipynb file in a python compatible editor (make sure all the files are in the same directory upon downloading)
- Run the code
- Provide a message you want to be encrypted
- Select the method of encryption by typing one of the following keys:    
&ensp;&ensp; ``` 1 ``` - Caesar cipher variant 1    
&ensp;&ensp; ``` 2 ``` - Caesar cipher variant 2    
&ensp;&ensp; ``` 3 ``` - Vigenere cipher    
&ensp;&ensp; ``` 4 ``` - Playfair cipher    
- The encrypted message will appear as an output. You will be asked if you want to decrypt this message. Type ```y``` (YES) or ```n``` (NO).

&ensp;&ensp;&ensp; For a better experience, please read and respect the technical specifications before trying to run the program:
- The cyphers were implemented only for the English alphabet. Do not use any other language symbols.
- The cyphers are programmed to understand only all-characters messages. Do not use numbers or any symbols, other than ``` . ``` upper or lower letters and spaces.

&ensp;&ensp;&ensp; If you want to test the code, you can see it in the testcode.ipynb file, carefully commented out.          
&ensp;&ensp;&ensp; In the following chapters, you can find more details regarding the implementation of each type of cypher.

## Caesar Cypher version 1
&ensp;&ensp;&ensp; Caesar cypher is a classical substitution cypher which consists of 3 major components:
1. The plain text that needs to be encrypted.
2. The key by which the alphabet will be permutated
3. The alphabet where each letter corresponds to a code (A-0, B-1,...,Z-25)

&ensp;&ensp;&ensp; Let's study how the cypher works with the following example of components:
+ Plain text: Hello.
+ key: 3
+ Alphabet: A->0, B->1 ,..., Z->25

Using these components, the cypher follows the steps:
1. Transforms the letter into a number:
- H -> 8
- e -> 5
- l -> 12
- l -> 12
- o -> 15
2. Increases that number by the key = 3 and divides it to 26 (respecting the range of numbers we have in an alphabet), which gets us the following list of numbers:   
***[ 11, 8, 15, 15, 18 ]***
3. Transforms those numbers back to letters according to the alphabet:
- 11 -> K
- 8 -> h
- 15 -> o
- 15 -> o
- 18 -> r

As a result, see below the output of the program:
```
Please introduce the text you would like to encrypt: Hello.

Consider the following classical ciphers:
1 - Caesar classic cipher
2 - Caesar cipher with random alphabet
3 - Vigenere cipher
4 - Playfair cipher

Please introduce the index of the cipher you would like to use: 1
Type the key for this message (a number): 3
The original message:
Hello.
The encrypted message:
Khoor.
```
Regarding the decryption algorithm, I will leave you with the fun of discovering it. Enjoy!

## Caesar Cypher version 2
&ensp;&ensp;&ensp; Caesar cypher version 2 is a classical substitution cypher which consists of the following 3 major components:
1. The plain text that needs to be encrypted.
2. The key by which the alphabet will be permutated
3. The randomised alphabet where each letter corresponds to a code.

&ensp;&ensp;&ensp; Let's study how the cypher works with the following example of components:
+ Plain text: Hello.
+ key: 3
+ Alphabet: KDOSQAWUFCYETNPIGRLZXBJVHM, where K->0, D->1,..., M->25

&ensp;&ensp;&ensp; Using these components, the cypher follows the steps:
1. Transforms the letter into their respective number in the random alphabet:
- H -> 24
- e -> 11
- l -> 18
- l -> 18
- o -> 2
2. Increases that number by the key = 3 and divides it to 26 (respecting the range of numbers we have in an alphabet), which gets us the following list of numbers:   
***[ 1, 14, 21, 21, 5]***
3. Transforms those numbers back to letters according to the random alphabet:
- 1 -> D
- 14 -> p
- 21 -> b
- 21 -> b
- 5 -> a

As a result, see below the output of the program:
```
Please introduce the text you would like to encrypt: Hello.

Consider the following classical ciphers:   
1 - Caesar classic cipher   
2 - Caesar cipher with random alphabet   
3 - Vigenere cipher   
4 - Playfair cipher   

Please introduce the index of the cipher you would like to use: 2
Type the key for this message (a number): 3

The secret random alphabet:
kdosqawufcyetnpigrlzxbjvhm

The original message:
Hello.
The encrypted message:
Dpbba.
```
Regarding the decryption algorithm, I will leave you with the fun of discovering it. Enjoy!
## Vigenere Cypher
&ensp;&ensp;&ensp; Vigenere cypher is a classical cypher, a little bit more complicated than the Caesar one, using a word as a key. It has the following components:
1. The plain text that needs to be encrypted
2. The key -> a word, where it's each letter's order in the alphabet is sequentially a key.
3. The alphabet where each letter corresponds to a code (A-0, B-1,...,Z-25)

&ensp;&ensp;&ensp; Let's study how the cypher works with the following example of components:
+ Plain text: Hello.
+ key: world
+ Alphabet: A->0, B->1 ,..., Z->25

&ensp;&ensp;&ensp; Using these components, the cypher follows the steps:
1. Transforms the letter into their respective number in the random alphabet:
- H -> 8
- e -> 5
- l -> 12
- l -> 12
- o -> 15
2. To each number add the order of each letter from the key:
- 8 + w = 8 + 23 = 31, 31 mod 26 = 5
- 5 + o = 5 + 15 = 20
- 12 + r = 12 + 18 = 30, 30 mod 26 = 4
- 12 + l = 12 + 12 = 24
- 15 + d = 15 + 4 = 19   
***[5, 20, 4, 24, 19]***
3. Transforms those numbers back to letters according to the random alphabet:
- 5 -> E
- 20 -> t
- 4 -> d
- 24 -> x
- 19 -> l

As a result, see below the output of the program:
```
Please introduce the text you would like to encrypt: Hello.

Consider the following classical ciphers:
1 - Caesar classic cipher
2 - Caesar cipher with random alphabet
3 - Vigenere cipher
4 - Playfair cipher

Please introduce the index of the cipher you would like to use: 3
Type the key for this message (a word): world
The original message:
Hello.
The encrypted message:
Etdxl.
```
Regarding the decryption algorithm, I will leave you with the fun of discovering it. Enjoy!
## Playfair Cypher
&ensp;&ensp;&ensp; Playfair cypher is a little bit more complex than the other 2, consisting of a 5x5 table where the letters in the key were first added, not repeated, and then the remaining letters of the alphabet.

&ensp;&ensp;&ensp; Let's study how the cypher works with the following example of components:
+ Plain text: Hello.
+ key: world
+ The resulting table (as there are only 25 cells, the letter J is omitted):

W | O | R | L | D
--- | --- | --- | --- | ---
A  | B | C | E | F
G  | H | I | K | M
N  | P | Q | S | T
U  | V | X | Y | Z

&ensp;&ensp;&ensp; Preparing for encryption, the cypher follows the steps:
1. Break the message into duos:   
***['He', 'll', 'o']***
2. Since the second duo consists of 2 letters, break it into single ones and the second one append it to the single letter 'o':   
***['He', 'l', 'lo']***
3. Add a bogus letter 'S' to the letters that are single:   
***['He', 'lS', 'lo']***
4. Transform all of them in upper letters:   
***['HE', 'LS', 'LO']***

&ensp;&ensp;&ensp; Now, when we are encrypting the duos by the table we have 3 cases:
1. Both letters are on the same row -> Substitute each letter with their right one
Case: In our example 'LO', 'L' and 'O' are in the first row.
Solution: 'L' -> D and 'O' -> R, therefore we have the duo DR
2. Both letters are on the same column> Substitute each letter with the one under them:
Case: In our example 'LS', 'L' and 'S' are in the 4th column.
Solution: 'L' -> E and 'S' -> Y, therefore we have the duo EY
3. Letters form a rectangle in the table -> Substitute each letter with the one from the opposite corner:

 .| . | . 
---|---|---
| *B* | C | **E** 
| **H** | I | *K* 


&ensp;&ensp;&ensp;&ensp; Case: In our example 'HE', 'H' and 'E' are in the corners of a rectangle.   
&ensp;&ensp;&ensp;&ensp; Solution: 'H'->K and 'E'->B, therefore we have KB   

&ensp;&ensp;&ensp; In the end, we obtain the encrypted list ***['HE', 'LS', 'LO'] -> ['KB', 'EY', 'DR']***
As a result, see below the output of the program:
```
Please introduce the text you would like to encrypt: Hello.

Consider the following classical ciphers:
1 - Caesar classic cipher
2 - Caesar cipher with random alphabet
3 - Vigenere cipher
4 - Playfair cipher

Please introduce the index of the cipher you would like to use: 4
Type the key for this message (a word): world
W -> 00
O -> 01
R -> 02
L -> 03
D -> 04
A -> 10
B -> 11
C -> 12
E -> 13
F -> 14
G -> 20
H -> 21
I -> 22
K -> 23
M -> 24
N -> 30
P -> 31
Q -> 32
S -> 33
T -> 34
U -> 40
V -> 41
X -> 42
Y -> 43
Z -> 44
The original message:
Hello.
The encrypted message:
KBEYDR
```
Regarding the decryption algorithm, I will leave you with the fun of discovering it. Enjoy!
## Conclusions
&ensp;&ensp;&ensp; Classical cyphers are definitely fun. There are tens of variations of those simple ones we saw above, but they all can be easily broken by any computer in mere seconds.    
&ensp;&ensp;&ensp; However, the brilliant minds that created those cyphers did undoubtedly put the foundation in modern cryptology. Although complex and hard to break, the modern cyphers still carry in them the seed of the logic behind the classical cyphers. 
