---
id: 2e8bbb09-0a24-438c-b21f-d4ec81933fde
name: Directory Brute Force a Web App with Extensions (GoBuster)
type: procedure
verified: true
submitted: true
created_at: '2019-10-10T21:55:34.655033+00:00'
updated_at: '2023-05-26T18:07:21.556975+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
platforms:
- Web
tags:
- '[[data exposure]]'
- '[[Network]]'
commands:
- '[[Gobuster Directory Brute Force with Extensions]]'
---

# Directory Brute Force a Web App with Extensions (GoBuster)

**Status**: ✓ Verified

## Summary

Perform a directory brute force while specifying extensions. Choose file extensions to brute force based on initial recon of  files on the webserver (.php, .asp, .js, etc), directories (cgi-bin suggests .sh scripts), underlying technology disclosed in headers (Python, PHP, Ruby), etc. For example, 

## Description

# Description

Perform a directory brute force while specifying extensions. Choose file extensions to brute force based on initial recon of  files on the webserver (.php, .asp, .js, etc), directories (cgi-bin suggests .sh scripts), underlying technology disclosed in headers (Python, PHP, Ruby), etc. For example, if a webserver is running IIS,  target extensions might be php, asp, aspx, and js.



# Instructions

1. Manually enumerate the web application with a browser and Burp proxy, noting file types, directories, technology, etc. 

2. Brute force files with extensions by specifying the "-x" argument followed by each extension.





**Command** ([[Gobuster Directory Brute Force with Extensions]]):

```bash
gobuster dir -w $_WORDLIST -u http://$_TARGET_IP -f -e -x '$_EXT1,$_EXT2,$_EXT3'
```





## Platforms

- Web

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]

## Commands Used

- [[Gobuster Directory Brute Force with Extensions]]

## Tags

- [[data exposure]]
- [[Network]]


