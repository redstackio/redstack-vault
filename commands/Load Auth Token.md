---
id: de4f4976-7d15-4b4c-bf03-9019ceaa403f
name: Load Auth Token
type: command
executor: bash
data: "import cPickle\nfrom base64 import b64decode\n\ndef load_token(token):\n  \
  \  return cPickle.loads(b64decode(token))\n\nauth_token = raw_input(\"Enter Auth\
  \ Token : \")\nuser = load_token(auth_token)"
output: null
created_at: '2023-04-06T03:55:59.484537+00:00'
updated_at: '2023-04-06T03:55:59.491985+00:00'
---

# Load Auth Token

```bash
import cPickle
from base64 import b64decode

def load_token(token):
    return cPickle.loads(b64decode(token))

auth_token = raw_input("Enter Auth Token : ")
user = load_token(auth_token)
```
