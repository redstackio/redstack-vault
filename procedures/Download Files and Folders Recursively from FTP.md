---
id: e1186806-ffd3-4aae-a1e9-ae02bef82b0f
name: Download Files and Folders Recursively from FTP
type: procedure
verified: false
submitted: false
created_at: '2019-10-25T23:22:29.971132+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
platforms:
- Linux
- Windows
tags:
- '[[data exposure]]'
- '[[file transfer]]'
- '[[Network]]'
commands:
- '[[Wget Download Recursively from FTP]]'
---

# Download Files and Folders Recursively from FTP

## Summary

Download files and folders recursively from an FTP site. It should be noted that this may result in significant traffic, and and should be avoided when stealth is required. 

## Description

# Description

Download files and folders recursively from an FTP site. It should be noted that this may result in significant traffic, and and should be avoided when stealth is required.

# Instructions

**Command** ([[Wget Download Recursively from FTP]]):

```bash
wget -r --no-passive --no-parent -m ftp://$_TARGET_IP
```

## Platforms

- Linux
- Windows

## Products

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

## Commands Used

- [[Wget Download Recursively from FTP]]

## Tags

- [[data exposure]]
- [[file transfer]]
- [[Network]]
