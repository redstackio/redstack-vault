---
id: b3ab27e6-8a3a-49ee-88c1-5e59a58a5945
name: Decrypt a Cisco Type 7 Password
type: procedure
verified: false
submitted: false
created_at: '2019-12-18T20:24:02.242469+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Cryptography]]'
- '[[data encryption]]'
commands:
- '[[ciscot7.py Decrypt a Cisco Type 7 Password]]'
---

# Decrypt a Cisco Type 7 Password

## Summary

Cisco router passwords encrypted using Type 7 are trivial to decrypt using open source tools, as the key is public. 

## Description

# Description

Cisco router passwords encrypted using Type 7 are trivial to decrypt using open source tools, as the key is public.



# Instructions

1. Download the Cisco Type 7 Password Decryptor: [Download from GitHub](https://github.com/theevilbit/ciscot7)

2. Identify Type 7 password. Sample:



**Code**: [[username admin privilege 15 password 7 02375012182]]





2. Decrypt the password



**Command** ([[ciscot7.py Decrypt a Cisco Type 7 Password]]):

```bash
python ciscot7.py -d -p $_PASSWORD
```





## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[ciscot7.py Decrypt a Cisco Type 7 Password]]

## Tags

- [[Cryptography]]
- [[data encryption]]


