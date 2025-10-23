---
id: 5130d68f-3348-474b-a11b-b76a9425c400
name: Enumerate LAPS artifacts local machine
type: procedure
verified: false
submitted: false
created_at: '2023-01-12T19:12:06.996469+00:00'
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
- '[[Enumerate LAPS artifact on local disk]]'
- '[[Enumerate LAPS file on local disk]]'
- '[[registry query for LAPS artifacts]]'
---

# Enumerate LAPS artifacts local machine

## Summary

LAPS has artifacts on a local machine, this can avoid querying the DC for OUs or GPOs to identify if LAPS is used. 

## Description

# Description

LAPS has artifacts on a local machine, this can avoid querying the DC for OUs or GPOs to identify if LAPS is used.



## Objective

1. Find local artifacts in registry

looking for AdmPwd

2. Find local artifacts on filesystem

looking for Admpwd.dll



# Instructions

1. Look at the registry for a key/value for AdmPwd





**Command** ([[registry query for LAPS artifacts]]):

```bash
reg query "HKLM\Software\Policies\Microsoft Services\AdmPwd" /v AdmPwdEnabled
```



2. Look at the filesystem for AdmPwd.dll, the file will exist if LAPS is used





**Command** ([[Enumerate LAPS artifact on local disk]]):

```bash
Get-ChildItem 'c:\program files\LAPS\CSE\Admpwd.dll'
```



(Alternative) Looking for LAPS file on local disk. 





**Command** ([[Enumerate LAPS file on local disk]]):

```bash
dir "C:\Program Files\LAPS\CSE\Admpwd.dll"

```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]

## Commands Used

- [[Enumerate LAPS artifact on local disk]]
- [[Enumerate LAPS file on local disk]]
- [[registry query for LAPS artifacts]]

## Tags

- [[Enumeration]]


