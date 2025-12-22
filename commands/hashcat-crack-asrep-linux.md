---
id: e6c02320-028c-44c4-8a2e-8f77ceb5d7be
name: hashcat-crack-asrep-linux
type: command
executor: bash
data: hashcat -m 18200 --force -a 0 $_HASH_FILE $_WORDLIST
output: null
created_at: '2023-04-06T03:56:04.983786+00:00'
updated_at: '2023-04-10T20:26:39.227036+00:00'
platforms:
  - Linux
tags:
  - cracking
  - hashcat
verified: true
validated: true
---

# hashcat-crack-asrep-linux

## Command

```bash
hashcat -m 18200 --force -a 0 $_HASH_FILE $_WORDLIST
```

## Description

Cracks Kerberos AS-REP hashes using dictionary attack on Linux.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m 18200 | Kerberos 5 AS-REP mode | Yes |
| --force | Ignore warnings | No |
| -a 0 | Dictionary attack | Yes |
| $_HASH_FILE | Input hash file | Yes |
| $_WORDLIST | Wordlist file | Yes |

## Examples

### Basic Usage

```bash
hashcat -m 18200 --force -a 0 hashes.asreproast passwords_kerb.txt
```

## Expected Output

Session... status, cracked passwords if successful.

## Related

- [[procedures/Kerberos-AS-REP-Roasting-Attack]]
- [[tools/Hashcat]]
