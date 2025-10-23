---
id: 703e292f-7a38-40f5-944e-50bc9a9e4e07
name: Encode data with JWT
type: command
executor: bash
data: 'import jwt

  public = open(''public.pem'', ''r'').read()

  print public

  print jwt.encode({"data":"test"}, key=public, algorithm=''HS256'')'
output: null
created_at: '2023-04-06T03:56:00.633610+00:00'
updated_at: '2023-04-10T20:22:33.490177+00:00'
---

# Encode data with JWT

```bash
import jwt
public = open('public.pem', 'r').read()
print public
print jwt.encode({"data":"test"}, key=public, algorithm='HS256')
```


