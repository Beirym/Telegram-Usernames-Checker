# Telegram-Usernames-Checker
Telegram Usernames Checker - is a controller for quickly checking a large number of nicknames in Telegram.

# Language:
    Python 3.10.4
    
# Libraries:
    1. requests
    2. datetime
    3. traceback
    4. bs4
    5. progress

# What is it intended for
    This script is necessary to quickly check a huge number of nicknames for Telegram for validity 
    (checking characters, availability, being on sale)
    
# How it works
    1. User create file and filling his words;
    2. User transmist file name to programm;
    3. Programm checks empty line for avability in the end of this file;
    4. Programm checks this word ( AKA our future username ) for avaibility in Telegram ( is he busy with other users )
    5. Programm checks this word for being on sale in Fragment.com
    6. Avaibility usernames saved in new file with title - avail_usernames_[time_(Year-Month-Day)]
