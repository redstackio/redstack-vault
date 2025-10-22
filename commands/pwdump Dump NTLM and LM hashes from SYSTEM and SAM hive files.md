---
id: 99bab2d9-679a-4234-9ce0-ee4562eb5f42
name: pwdump Dump NTLM and LM hashes from SYSTEM and SAM hive files
type: command
executor: ''
data: pwdump SYSTEM SAM
output: "root@kali:~# pwdump system sam \nAdministrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::\n\
  Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::\n\
  BOB:1000:aad3b435b51404eeaad3b435b51404ee:dc265511a1d1a7a3ce6f6d2a3fb6bbe1:::"
created_at: '2019-09-26T22:51:06.757650+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# pwdump Dump NTLM and LM hashes from SYSTEM and SAM hive files

```bash
pwdump SYSTEM SAM
```

## Expected Output

```
root@kali:~# pwdump system sam 
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
BOB:1000:aad3b435b51404eeaad3b435b51404ee:dc265511a1d1a7a3ce6f6d2a3fb6bbe1:::
```
