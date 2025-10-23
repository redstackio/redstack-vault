---
id: 404e65ee-25cc-4681-ac06-f16c5e6a4e7c
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:19.219164+00:00'
updated_at: '2023-04-10T20:34:32.000164+00:00'
---

# Code Snippet 404e65ee

**Language**: Powershell

```powershell
openssl passwd -1 -salt hacker hacker
mkpasswd -m SHA-512 hacker
python2 -c 'import crypt; print crypt.crypt("hacker", "$6$salt")'
```


