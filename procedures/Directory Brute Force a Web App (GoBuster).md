---
id: 905b31b9-e98a-40fe-886d-206b65c4b50b
name: Directory Brute Force a Web App (GoBuster)
type: procedure
verified: true
submitted: true
created_at: '2020-03-16T04:55:06.453822+00:00'
updated_at: '2023-05-26T01:27:16.281918+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
platforms:
- Web
tags:
- '[[Enumeration]]'
- '[[Web Applications]]'
commands:
- '[[Gobuster Directory Brute Force]]'
---

# Directory Brute Force a Web App (GoBuster)

**Status**: ✓ Verified

## Summary

Enumerate a website's files and folders by performing a dictionary brute force on possible file and folder names. 

## Description

# Description

Enumerate a website's files and folders by performing a dictionary brute force on possible file and folder names.

# Instructions

**Command** ([[Gobuster Directory Brute Force]]):

```bash
gobuster dir -w $_WORDLIST -u http://$_TARGET_IP
```

## Platforms

- Web

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]

## Commands Used

- [[Gobuster Directory Brute Force]]

## Tags

- [[Enumeration]]
- [[Web Applications]]
