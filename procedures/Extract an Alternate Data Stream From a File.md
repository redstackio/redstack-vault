---
id: 6d8de39e-862e-41b3-85b5-61ffb92a8f50
name: Extract an Alternate Data Stream From a File
type: procedure
verified: false
submitted: false
created_at: '2019-11-22T18:04:45.451961+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[NTFS File Attributes|T1096 - NTFS File Attributes]]'
platforms:
- Windows
tags:
- '[[File System]]'
- '[[Obfuscation]]'
commands:
- '[[Extract ADS Embedded Data from a File (PowerShell)]]'
- '[[List Directory Contents Including ADS]]'
- '[[more Extract ADS Embedded Data from a File]]'
---

# Extract an Alternate Data Stream From a File

## Summary

Alternate Data Strems are a feature of NTFS (3.1+) which allows more than one data stream to be associated with a file. Since this additional data stream is not listed by default in explorer.exe, command line file listing, or reflected in file size itself, it can be a simple method to obfuscating f

## Description

# Description

Alternate Data Strems are a feature of NTFS (3.1+) which allows more than one data stream to be associated with a file. Since this additional data stream is not listed by default in explorer.exe, command line file listing, or reflected in file size itself, it can be a simple method to obfuscating files, though is not hard to detect. 

# Instructions

## Verify the ADS Stream Name

**Command** ([[List Directory Contents Including ADS]]):

```bash
dir /R
```

In this example, the stream is named 'secret'

## Extract ADS using cmd.exe

**Command** ([[more Extract ADS Embedded Data from a File]]):

```bash
more < $_FILE:$_ADS
```

## Extract ADS using PowerShell.exe

**Command** ([[Extract ADS Embedded Data from a File (PowerShell)]]):

```bash
Get-Content -Path $_FILE -stream $_ADS
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[NTFS File Attributes|T1096 - NTFS File Attributes]]

## Commands Used

- [[Extract ADS Embedded Data from a File (PowerShell)]]
- [[List Directory Contents Including ADS]]
- [[more Extract ADS Embedded Data from a File]]

## Tags

- [[File System]]
- [[Obfuscation]]
