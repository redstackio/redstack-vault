---
id: fa528ab6-8d18-428c-bb1a-6952e8531cf2
name: Invisi-Shell hide powershell scripts
type: procedure
verified: false
submitted: false
created_at: '2023-01-12T04:43:16.991778+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Windows
tags:
- '[[Defense Bypass]]'
commands:
- '[[Inivis-shell hide powershell scripts (admin)]]'
- '[[Invisi-shell hide powershell scripts (non admin)]]'
- '[[Load Powershell]]'
---

# Invisi-Shell hide powershell scripts

## Summary

Bypass powershell security features and hide your powershell script in plain sight. Use this before running other scripts or commands on the powershell terminal. It only functions in the current powershell console session this is executed on. - ScriptBlock logging - Module Logging - Transcription -

## Description

# Description

Bypass powershell security features and hide your powershell script in plain sight. Use this before running other scripts or commands on the powershell terminal.

It only functions in the current powershell console session this is executed on.



- ScriptBlock logging

- Module Logging

- Transcription

- AMSI



[Invisi-Shell](https://github.com/OmerYa/Invisi-Shell)



## Objective

1. Hide powershell scripts from security features and logging



# Instructions

1. Execute from CMD prompt

Non-Admin user type:





**Command** ([[Invisi-shell hide powershell scripts (non admin)]]):

```bash
RunWithRegistryNonAdmin.bat
```





Admin user type:



**Command** ([[Inivis-shell hide powershell scripts (admin)]]):

```bash
RunWithPathAsAdmin.bat
```





2. Load a powershell prompt from the same CMD prompt





**Command** ([[Load Powershell]]):

```powershell
powershell
```





## Platforms

- Windows

## Commands Used

- [[Inivis-shell hide powershell scripts (admin)]]
- [[Invisi-shell hide powershell scripts (non admin)]]
- [[Load Powershell]]

## Tags

- [[Defense Bypass]]


