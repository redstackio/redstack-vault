---
id: 69b954c2-c5c2-4734-9756-b96bbcd7b337
name: Embed an Alternate Data Stream (ADS) in a File
type: procedure
verified: true
submitted: true
created_at: '2019-11-22T17:24:23.178077+00:00'
updated_at: '2023-05-25T20:02:53.961708+00:00'
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
- '[[Add-Content Embed a Data Stream Within a File]]'
- '[[Embed an Alternate Data Stream into a File]]'
---

# Embed an Alternate Data Stream (ADS) in a File

**Status**: ✓ Verified

## Summary

Alternate Data Strems are a feature of NTFS introduced in Windows NT 3.1, which allows more than one data stream to be associated with a file, effectively hiding a file (embedded file), within another (cover file). Since this additional data stream is not listed by default in explorer.exe, command 

## Description

# Description

Alternate Data Strems are a feature of NTFS introduced in Windows NT 3.1, which allows more than one data stream to be associated with a file, effectively hiding a file (embedded file), within another (cover file). Since this additional data stream is not listed by default in explorer.exe, command line file listing, or reflected in file size itself, it can be a simple method to obfuscating files, though is not hard to detect.





# Instructions

Identify the file which will be embedded, and the file which will hide the stream 



## Command Prompt (cmd.exe)





**Command** ([[Embed an Alternate Data Stream into a File]]):

```bash
type $_EMBEDDED_FILE > $_COVER_FILE:secret
```



Note: it is also possible to echo text directly into an ADS rather than using type.





## PowerShell





**Command** ([[Add-Content Embed a Data Stream Within a File]]):

```bash
Add-Content -Path $_COVER_FILE -Value "Hidden Data" -Stream $_EMBEDDED_FILE
```





## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[NTFS File Attributes|T1096 - NTFS File Attributes]]

## Commands Used

- [[Add-Content Embed a Data Stream Within a File]]
- [[Embed an Alternate Data Stream into a File]]

## Tags

- [[File System]]
- [[Obfuscation]]


