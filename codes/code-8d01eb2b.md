---
id: 8d01eb2b-3771-40f4-a232-82c0a9a8d440
type: code
language: Python
verified: false
created_at: '2023-04-06T03:55:59.484467+00:00'
updated_at: '2023-04-06T03:55:59.491915+00:00'
---

# Code Snippet 8d01eb2b

**Language**: Python

```python
import cPickle
from base64 import b64decode

def load_token(token):
    return cPickle.loads(b64decode(token))

auth_token = raw_input("Enter Auth Token : ")
user = load_token(auth_token)
print "Welcome {}".format(user.username)
```
