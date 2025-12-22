---
id: e6c02320-028c-44c4-8a2e-8f77ceb5d7be
name: hashcat-crack-asrep-windows
type: command
executor: bash
data: hashcat64.exe -m 18200 '$_HASH_STRING' -a 0 $_WORDLIST_PATH
output: null
created_at: '2023-04-06T03:56:04.983786+00:00'
updated_at: '2023-04-10T20:26:39.227036+00:00'
platforms:
  - Windows
tags:
  - cracking
  - hashcat
verified: true
validated: true
---

# hashcat-crack-asrep-windows

## Command

```bash
hashcat64.exe -m 18200 '$_HASH_STRING' -a 0 $_WORDLIST_PATH
```

## Description

Windows variant for cracking AS-REP hashes with Hashcat.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m 18200 | AS-REP mode | Yes |
| '$_HASH_STRING' | Inline hash or file | Yes |
| -a 0 | Dictionary mode | Yes |
| $_WORDLIST_PATH | Path to wordlist | Yes |

## Examples

### Basic Usage

```bash
hashcat64.exe -m 18200 '<AS_REP-hash>' -a 0 c:\wordlists\rockyou.txt
```

## Expected Output

Cracking progress and results.

## Related

- [[procedures/Kerberos-AS-REP-Roasting-Attack]]
- [[tools/Hashcat]]
