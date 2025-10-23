---
id: 25907b4f-1a00-4eb3-9b80-984102fa1185
name: john
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:51.426558+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# john



**Command** ([[crack as_rep_response_file (asreproast)]]):

```bash
john --wordlist=passwords_file as_rep_response_file

```







**Command** ([[crack as_rep_response_file (kerberoast)]]):

```bash
john --format=krb5tgs --wordlist=passwords_file AS_REP_responses_file

```







**Command** ([[mangle wordlist]]):

```bash
john --wordlist=month --rules --stdout > new_list

```







**Command** ([[crack ssh keys]]):

```bash
/usr/share/john/ssh2john.py id_rsa > hash.john
john --wordlist=/usr/share/wordlists/rockyou.txt hash.john

```






