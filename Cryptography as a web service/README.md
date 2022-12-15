# Laboratory Work Nr. 5                
### Course: Cryptography & Security                
### Author: Gîlca Constantina                
                
----                
                
## Topic: # Web Authentication & Authorization                      
&ensp;&ensp;&ensp; **Authentication & Authorization** are 2 of the main security goals of IT systems and should not be used interchangeably. Simply put, during authentication the system verifies the identity of a user or service, and during authorization, the system checks the access rights, optionally based on a given user role.                
                               
## Objectives                       
* To implement, with the scope of better understanding the terms and the process of Authentication and Authorization, implement the previous laboratories in a web service project where the user should first authenticate and then get authorized access to the services provided *(used Postman for Registration and User Authentication)*                       
* To implement the theory knowledge gathered in the course lessons, in practice.                       
                       
## Technical Specifications                
&ensp;&ensp;&ensp; The laboratory work was implemented in Python v3.9.2. You can test the implementation by following the next steps:                       
- Download the entire `Cryptography as a web service` directory.                       
- Open the command line and enter the directory where the files are located.                
- Run the following line:                
`python main.py`                
                           
&ensp;&ensp;&ensp; If you want to see the code, access the files in a python compatible editor and you will see the implementation. For a better understanding, an example is analysed in the following chapter.                       
                       
&ensp;&ensp;&ensp; The cyphers used are from the previous laboratory works. You can find them in their specified folders on this repository. You can find more details regarding each implementation in the reports of the specific cyphers.                      
                       
## Authentication and Authorization                      
&ensp;&ensp;&ensp; The services that the server provides are the following:                
1. Registration of new users                
2. Authentication of existing users                
3. Access authorization                
4. Play with the implemented ciphers                
                
&ensp;&ensp;&ensp; First thing, we have the **Registration of the user**. The server accepts POST requests with data as in the following example:                
```                
{                
     "Name" : "Constantina",                
     "Surname" : "Gîlca",                
     "Email" : "constantina.gilca@isa.utm.md",                
     "Password" : "password2",                
     "Access":"Basic"                
}                
```                
&ensp;&ensp;&ensp; In the `Security Lab5.postman_collection.json` file, you will find a collection of requests you can send to the server using Postman. The first 3 ones are POST types for user registration. If you will try to use them, you will get an error since the database `users.db` already has those users saved. If you want, you can delete the database and restart the server, it will create the database from scratch. Then you can try the POST requests, they will work.                
                
&ensp;&ensp;&ensp;The database stores the Name, Surname, Email and Access fields as strings the same way as they are in the request. Regarding the Password, however, the server hashes it by using the argon2 python library and saves the hash of the password.                
                
&ensp;&ensp;&ensp; Then comes the **Log In of the user**. The server accepts GET requests with data as in the following example:                
```                
{                
     "Email" : "constantina.gilca@isa.utm.md",                
     "Password" : "password2"                
}                
```                
&ensp;&ensp;&ensp; In the `Security Lab5.postman_collection.json` file, you will find a collection of GET requests you can send to the server for login. Just make sure before you send them that the users are registered in the database, otherwise, you will get a 404 error.                 
                                      
&ensp;&ensp;&ensp; What the server does then is it first hashes the password and verifies it with the hash from the database. If the hash is a match, the server proceeds on finding the user in the database by email address. If the email is written wrong or the database does not hold such a user you will get a 404 error: User not found.                 
                
&ensp;&ensp;&ensp; Even if the user is in the database and the password's hash matches the one in the database since we are implementing Multi-Factor Authentication, we need another way to verify the user's identity. Therefore, we are generating a **counter based one-time password** through the python library pyotp (more on https://pyauth.github.io/pyotp/#) of a random index from 0 to 2000. The generated code consists of 6 digits. Then, the server sends the code through email to the email address of the user. The user has to type in the command line the 6-digit code in order to get their access in the system approved. If the 6 digits code introduced matches the server-generated one, the user has access to the system.                
                
&ensp;&ensp;&ensp; Now that the Authentication is done, the server has to **Authorize the access of the user to the specific data**. We have 2 types of access, Premium and Basic. The types are specified in the requests when the users are registered. based on the field Access in the database, the user gets access to either the *PlayBasic* class, which offers access only to the classical cyphers to be used, or the *PlayPremium* class, which offers access to all types of cyphers, including the digital signature example implemented in laboratory work nr.4.                
                
&ensp;&ensp;&ensp; For example, if we register the following user in the database:                
```                
{                
     "Name" : "Constantina",                
     "Surname" : "Gîlca",                
     "Email" : "constantina.gilca@isa.utm.md",                
     "Password" : "password2",                
     "Access":"Basic"                
}                
```                
and we try to log in with the following data:                
```                
{                
     "Email" : "constantina.gilca@isa.utm.md",                
     "Password" : "password2"                
}                
```                
the *PlayBasic* class will be instantiated, which will print the following:                
```                
Welcome dear Constantina !                
Let's Play!                
        What cipher would you like to use?                
                
        1 - Classic Ceasar Cipher                
        2 - Random Alphabet Ceasar Cipher                
        3 - Vigenere Cipher                
        4 - Playfair Cipher                
                
        99 - to exit                
                
Type a number from 1 to 4:                
```                
It will wait for your input and then proceed to the cypher class of your choosing, or exit the program.                
                
If you try to enter as the same user, with the following information:                
```                
{                
     "Email" : "constantina.gilca@isa.utm.md",                
     "Password" : "wrongpassword"                
}                
```                
you will get the error `argon2.exceptions.VerifyMismatchError: The password does not match the supplied hash`, which means the password you provided is incorrect.                
                
Now if you register the user:                
```                
{                
     "Name" : "Ana",                
     "Surname" : "Gîlca",                
     "Email" : "constantinagilca@gmail.com",                
     "Password" : "password1",                
     "Access":"Premium"                
}                
```                
and you try to login with the request:                
```                
{                
     "Email" : "constantinagilca@gmail.com",                
     "Password" : "password1"                
}                
```                
the *PlayPremium* class will be instantiated, which will print the following:                
```                
Welcome dear Ana !                
Let's Play!                
        What would you like to play with?                
        1 - Classic Ciphers (ex: Caeser, Vigenere, Playfair)                
        2 - Symmetric Ciphers (ex: Blowfish,Rabbit)                
        3 - Asymmetric Ciphers (Diffie-Halman)                
        4 - Digital Signatures                
                
        10 - if you want to quit                
                
Type here from 1 to 4:        
```               
The server will wait for your input and then it will proceed with the class you chose to play.                         

## Conclusions       
&ensp;&ensp;&ensp; Authentication and Authorization are 2 different processes in the access management of the application, but they are often mistaken for each other. Authentication assures that the user entering the application is actually the one that has the right to enter, by providing sensible accurate data when entering the app. Authorization on the other hand assures that the user that entered got the access and rights attributed to them, no more and no less.                     
&ensp;&ensp;&ensp; The authentication happens on the outer layer of the application, interacting with the user, while the authorization takes place usually under the hood of the application and users do not know what is the process of granting the access they deserve.                   
&ensp;&ensp;&ensp; In the end, both processes are equally important and there are many ways to assure their integrity and success. We show merely a small part of the possibilities that are there regarding validating user data and granting access.          

