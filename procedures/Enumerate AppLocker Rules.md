---
id: 6df7d997-8b79-405f-8d3c-6aa17758050b
name: Enumerate AppLocker Rules
type: procedure
verified: true
submitted: true
created_at: '2020-03-04T05:01:54.843816+00:00'
updated_at: '2023-05-25T19:47:41.193609+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Security Software Discovery|T1063 - Security Software Discovery]]'
platforms:
- Windows
tags:
- '[[applocker]]'
- '[[Enumeration]]'
commands:
- '[[Export AppLocker Rules in XML]]'
- '[[xmllint Beautify XML]]'
---

# Enumerate AppLocker Rules

**Status**: ✓ Verified

## Summary

AppLocker rules permit or deny the execution of scripts (.ps1, .bat, .cmd, .vbs, .js), executables (.exe, .com), Windows Installer files (..msi, .msp, .mst), Packaged apps, and DLL files (.dll, .ocx). If configured, the rules can be viewed by unprivileged users. 

## Description

# Description

AppLocker rules permit or deny the execution of scripts (.ps1, .bat, .cmd, .vbs, .js), executables (.exe, .com), Windows Installer files (..msi, .msp, .mst), Packaged apps, and DLL files (.dll, .ocx). If configured, the rules can be viewed by unprivileged users.

# Instructions

1. List AppLocker rules in XML format. Omit the "-Xml" argument if more concise non-XML output is preferred

**Command** ([[Export AppLocker Rules in XML]]):

```powershell
powershell -nop -c "Import-Module AppLocker; Get-AppLockerPolicy -Effective -Xml"
```

2. (Optional) Copy/paste the XML onto a Linux host and use a beautifier on the XML output

**Command** ([[xmllint Beautify XML]]):

```bash
xmllint --format - < $_FILE.xml
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Security Software Discovery|T1063 - Security Software Discovery]]

## Commands Used

- [[Export AppLocker Rules in XML]]
- [[xmllint Beautify XML]]

## Tags

- [[applocker]]
- [[Enumeration]]
