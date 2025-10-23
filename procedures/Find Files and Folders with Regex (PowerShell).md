---
id: d36c250a-f406-4320-8854-4b3988febb26
name: Find Files and Folders with Regex (PowerShell)
type: procedure
verified: true
submitted: true
created_at: '2020-04-24T18:25:00.614353+00:00'
updated_at: '2023-05-25T19:59:03.472098+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
platforms:
- Windows
tags:
- '[[Enumeration]]'
commands:
- '[[Find Files and Folder with Regex (PowerShell)]]'
---

# Find Files and Folders with Regex (PowerShell)

**Status**: ✓ Verified

## Summary

Use native PowerShell cmdlets to search for files and folders by name, with support for regular expressions. This functions in a similar way to Linux/Unix's "find" command. 

## Description

# Description

Use native PowerShell cmdlets to search for files and folders by name, with support for regular expressions. This functions in a similar way to Linux/Unix's "find" command.



# Instructions





**Command** ([[Find Files and Folder with Regex (PowerShell)]]):

```bash
Get-ChildItem -Recurse | Where Name -Match "$_REGEX"
```







## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]

## Commands Used

- [[Find Files and Folder with Regex (PowerShell)]]

## Tags

- [[Enumeration]]


