---
id: 25e3f6b9-1833-4eba-af0d-3b6d7be81ce6
name: Directory Brute Force a Web App (Wfuzz)
type: procedure
verified: false
submitted: false
created_at: '2019-09-11T22:12:51.778764+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
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
- '[[Wfuzz Directory Brute Force]]'
---

# Directory Brute Force a Web App (Wfuzz)

## Summary

Enumerate a webs app's files and folders by performing a dictionary brute force attack. 

## Description

# Description

Enumerate a webs app's files and folders by performing a dictionary brute force attack.



# Instructions





**Command** ([[Wfuzz Directory Brute Force]]):

```bash
wfuzz --hc 404 -c -w $_WORDLIST -u http://$_TARGET_IP/FUZZ
```





## Platforms

- Web

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]

## Commands Used

- [[Wfuzz Directory Brute Force]]

## Tags

- [[Enumeration]]
- [[Web Applications]]


