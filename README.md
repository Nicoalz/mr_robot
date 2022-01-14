# Mr Robot Project - Nicolas BORDEAUX ⚙️


![Mr. Robot](https://www.meme-arsenal.com/memes/bc24ad66818046c60de806193b18f044.jpg)

## Table of Contents 🗃
* [Description](#description-)
* [Technology](#technology-)
* [How It Works](#how-it-works-)




## Description 📝
*These algorithms respond to 4 exercises :*
* A Luhn validated card generator
* A password generator
* A md5 brut force tester
* A binary to hexadecimal converter

## Technology 🔧
This project was all made with python.


## How It Works 🛠️

* ### ex01_card_generator.py :
Enter the type of card you want between "Visa" and "Mastercard" and you'll get (the numbers of) a luhn validated card. <br>
If you choose Visa, the card will begin by a 4. <br>
If you choose Mastercard, the card will begin by a 5. <br>
If you do not write visa or mastercard correctly, you will be prompted to retake your choice. <br>
This algorithm takes your choice as a parameter and then generates 15 digits randomly. These 16 ('4' or '5' + 15 randoms digits) digits are tested, if they do not respond to the Luhn algorithm, then 15 new digits will be generated, until it is validated.

* ### ex02_password_generator.py :
Enter the length you want for your password and you'll get a random password (letters and digits) of the length you have chosen. <br>
This algorithm generate a random character (between upper case letter, lower case letter and digits) for your password until it gets the length you have chosen.

* ### ex03_pin_code.py :
Enter the md5 hashed password you want and you'll get the original decrypted password.
This algorithm is programmed to decrypt an 8 digits code only. <br>
It takes your md5 hashed password as a parameter and hash every combination of 8 digits; from 00000000 to 99999999. <br>
If a combination hashed correspond to the hashed password you entered, it will return the original combination of 8 digits, so you have the decrypted password <br>
If there is no match, you will be prompted to verify that your hashed password is correct (from an 8 digits password).

* ### ex04_binary_to_hexa.py :
Enter the binary you want and you'll get it converted into hexadecimal.
This algorithm takes your input as a parameter and firstly verify that it's correctly written in binary (multiple of 4 and only with 0 and 1). <br>
Then it converts the binary to hexadecimal. It returns starting by the third character to not display '0x'.

<hr>

## Thanks for reading ! 