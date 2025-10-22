---
id: bb9bf9ec-dfdc-4ebf-9d0e-b463679db0da
name: Enumerate GPO with LAPS (Credentials)
type: procedure
verified: false
submitted: false
created_at: '2023-01-12T19:13:43.796117+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Permission Groups Discovery|T1069 - Permission Groups Discovery]]'
platforms:
- Windows
tags:
- '[[Enumeration]]'
commands:
- '[[Enumerate GPO for *laps in name]]'
---

# Enumerate GPO with LAPS (Credentials)

## Summary

Laps can be enumerated through GPOs on the Domain 

## Description

# Description

Laps can be enumerated through GPOs on the Domain

## Objective

1. Enumerate GPOs with LAPS wildcard in name

# Instructions

1. Look for GPO with LAPS in Identity name

**Command** ([[Enumerate GPO for *laps in name]]):

```bash
Get-DomainGPO | ? { $_.DisplayName -like "*laps*" } | select DisplayName, Name, GPCFileSysPath | fl
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]

## Commands Used

- [[Enumerate GPO for *laps in name]]

## Tags

- [[Enumeration]]
