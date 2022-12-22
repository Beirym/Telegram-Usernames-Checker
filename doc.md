# Documentation


## check_usernames 

**check_usernames** - basic function in program. She accepts 3 arguments - _words_array_, _usernames_output_, _progress_bar_

**words_array**

    Accepts file name or python list
    
**usernames_output**

    Accepts string "file" or "list"
    
**progress_bar**

    Accepts boolean True or False
    
    True - progress bar will be shown in terminal
    False - progress bar hidden
    
    Default - False

### Example
```python
from  telegram_usernames_checker.telegram_usernames_checker import check_usernames

availibale_usernames = check_usernames(words_array=['Beirym', 'durov', 'unique_username'], usernames_output='list')

print(availibale_usernames) # ['unique_username']
```
