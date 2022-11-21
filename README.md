# Telegram-Usernames-Checker
Telegram Usernames Checker - is a controller for quickly checking a large number of nicknames in Telegram.

# Language
    Python 3.10.4
    
# Instalation
    pip install telegram-usernames-checker
    
# Libraries
    1. requests
    2. datetime
    3. traceback
    4. bs4
    5. progress

# What is it intended for
    This script is necessary to quickly check a huge number of nicknames for Telegram for validity 
    (checking characters, availability, being on sale)
    
The idea of creation this program walked for me after appearence auction of nicknames in Telegram. As soon as Telegram gave users the opportunity to sell their nicknames, it became very difficult to find a good nickname for their account. There are situations when there are a lot of good nicknames in your head, but it takes a lot of time to check their availability. Telegram often starts to blunt during checking. Because of this, I decided to make this checker, which checks a large number of nicknames in a matter of minutes.
    
# How it works

This program takes user file contains nicknames, checking symbols in nickname, enter to t.me/username in order to check avaibility ( if nickname already busy, that in website don't will be HTML-element ( with class tgme_page_extra ) which contains nickname ). Next check it's checking for being on auction in Fragment.com ( if nicname don't being in auction, that website don't have seperate HTML-page for him ). If nickname passed all checks, that he inserted to list contains checked words. After all words checks user will receive file with all availible nicknames.
    
# Usage steps
    1. User create file and filling his words;
    2. User transmist file name to programm;
    3. Program checks empty line for avability in the end of this file;
    4. Program checks this word ( AKA our future username ) for avaibility in Telegram ( is he busy with other users );
    5. Program checks this word for being on sale in Fragment.com;
    6. Avaibility usernames saved in new file with title - avail_usernames_[Hours-Minutes_(Year-Month-Day)].
	
# Disadvanatges

	The program cannot check the nickname reserved by Telegram itself (these are nicknames when trying to use which Telegram gives an error - "Ivalid link")

# Important

It's fun programm, which is not used in real projects.
	
	
