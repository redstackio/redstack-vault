---
id: a8d1401a-66dd-413a-9c1b-0105d2db8a85
name: Brute Force an SNMP Community String
type: procedure
verified: true
submitted: true
created_at: '2019-10-18T21:24:21.445003+00:00'
updated_at: '2023-05-26T00:39:35.006356+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Service Discovery|T1007 - System Service Discovery]]'
platforms:
- Linux
- Windows
tags:
- '[[Brute Force]]'
- '[[Network]]'
commands:
- '[[Brute Force SNMP Community String]]'
---

# Brute Force an SNMP Community String

**Status**: ✓ Verified

## Summary

Simple Network Management Protocol (SNMP) is used for the exchange of management information between network devices. While protected with a community string for authorization, the string can be brute forced, allowing attackers to enumerate system services, patches, and other internal information. 

## Description

# Description

Simple Network Management Protocol (SNMP) is used for the exchange of management information between network devices. While protected with a community string for authorization, the string can be brute forced, allowing attackers to enumerate system services, patches, and other internal information.



# Instructions





**Command** ([[Brute Force SNMP Community String]]):

```bash
onesixtyone -c $_WORDLIST $_TARGET_IP
```





## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Service Discovery|T1007 - System Service Discovery]]

## Commands Used

- [[Brute Force SNMP Community String]]

## Tags

- [[Brute Force]]
- [[Network]]


