#Matching a String Against a Regular Expression With matches()

import re
stg="Wishe:Hello Developers"

match=re.match(r"Wishe:\w\w\w",stg)
print(match)
