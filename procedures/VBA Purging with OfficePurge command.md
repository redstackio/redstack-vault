---
id: c59a05e2-95e5-43ec-ad37-c5ad756de4fe
name: VBA Purging with OfficePurge command
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.795281+00:00'
updated_at: '2023-04-10T20:36:50.802301+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Office - Attacks]]'
- '[[OfficePurge]]'
- '[[VBA Purging]]'
commands:
- '[[OfficePurge.exe -d excel -f .\payroll.xls -m Module1]]'
- '[[OfficePurge.exe -d publisher -f .\donuts.pub -m ThisDocument]]'
- '[[OfficePurge.exe -d word -f .\malicious.doc -l]]'
- '[[OfficePurge.exe -d word -f .\malicious.doc -m NewMacros]]'
---

# VBA Purging with OfficePurge command

## Summary

VBA Purging is a technique used by attackers to remove macros from Office documents to avoid detection by security solutions. OfficePurge is a command that can be used to remove VBA macros from Office documents. This technique is often used in conjunction with other methods to avoid detection. By r

## Description

# Description

VBA Purging is a technique used by attackers to remove macros from Office documents to avoid detection by security solutions. OfficePurge is a command that can be used to remove VBA macros from Office documents. This technique is often used in conjunction with other methods to avoid detection. By removing the VBA macros, the attacker can make it more difficult for security solutions to detect malicious activity. 

Technical Details: The OfficePurge command is a tool that can be used to remove VBA macros from Office documents. It works by modifying the Office file to remove the VBA project. This tool can be used to remove VBA macros from Word, Excel, and PowerPoint documents. 

Business Value: Attackers use VBA Purging to avoid detection and increase the success rate of their attacks. By removing the VBA macros, they can make it more difficult for security solutions to detect and block their malicious activity. This can lead to successful attacks and data breaches. 

## Requirements

1. Access to Office documents with VBA macros

1. OfficePurge command line tool

## Defense

1. Keep Office software up to date with the latest security patches

1. Use anti-virus software to detect and block malicious activity

1. Educate users on the risks of opening Office documents from untrusted sources

## Objectives

1. To remove VBA macros from Office documents to avoid detection by security solutions

1. To increase the success rate of attacks by making it more difficult for security solutions to detect and block malicious activity

# Instructions

1. Use the OfficePurge command followed by the appropriate arguments to remove compressed VBA code from Office documents and execute malicious macros without many of the VBA keywords that AV engines rely on for detection.

**Code**: [[OfficePurge.exe -d word -f .\malicious.doc -m NewM]]

> The OfficePurge command can be used to remove compressed VBA code from various types of Office documents such as Word, Excel, and Publisher. The '-d' argument is used to specify the type of Office document. The '-f' argument is used to specify the file path of the document to be purged. The '-m' argument is used to specify the macro name to be executed after the purge. The '-l' argument is used to list the available macros in the specified document. This command can be used by attackers to bypass detection by AV engines and execute malicious macros.

**Command** ([[OfficePurge.exe -d word -f .\malicious.doc -m NewMacros]]):

```bash
OfficePurge.exe -d word -f .\malicious.doc -m NewMacros
```

**Command** ([[OfficePurge.exe -d excel -f .\payroll.xls -m Module1]]):

```bash
OfficePurge.exe -d excel -f .\payroll.xls -m Module1
```

**Command** ([[OfficePurge.exe -d publisher -f .\donuts.pub -m ThisDocument]]):

```bash
OfficePurge.exe -d publisher -f .\donuts.pub -m ThisDocument
```

**Command** ([[OfficePurge.exe -d word -f .\malicious.doc -l]]):

```bash
OfficePurge.exe -d word -f .\malicious.doc -l
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[OfficePurge.exe -d excel -f .\payroll.xls -m Module1]]
- [[OfficePurge.exe -d publisher -f .\donuts.pub -m ThisDocument]]
- [[OfficePurge.exe -d word -f .\malicious.doc -l]]
- [[OfficePurge.exe -d word -f .\malicious.doc -m NewMacros]]

## Tags

- [[Office - Attacks]]
- [[OfficePurge]]
- [[VBA Purging]]
