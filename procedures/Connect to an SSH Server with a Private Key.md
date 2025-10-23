---
id: 19d1316e-a40d-44fd-8df2-eb33a2edede4
name: Connect to an SSH Server with a Private Key
type: procedure
verified: true
submitted: true
created_at: '2019-11-25T20:01:51.981244+00:00'
updated_at: '2023-05-26T00:46:10.649666+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Valid Accounts|T1078 - Valid Accounts]]'
tags:
- '[[Network]]'
commands:
- '[[ssh Connect with a Private Key]]'
---

# Connect to an SSH Server with a Private Key

**Status**: ✓ Verified

## Summary

Use SSH to connect to a remote SSH server using a private key. 

## Description

# Description

Use SSH to connect to a remote SSH server using a private key.



# Instructions





**Command** ([[ssh Connect with a Private Key]]):

```bash
ssh -i $_PRIVATE_KEY -l $_USER $_TARGET_IP
```





## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Valid Accounts|T1078 - Valid Accounts]]

## Commands Used

- [[ssh Connect with a Private Key]]

## Tags

- [[Network]]


