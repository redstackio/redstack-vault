---
id: d0a77568-8751-435e-a7e7-102256247007
name: hashcat-brute-force-as-rep-hashes
type: command
executor: bash
data: hashcat -m 18200 $_HASH_FILE.txt $_WORDLIST.txt -O
output: |-
  hashcat (v6.2.6) starting...
  Session..........: hashcat
  Status...........: Cracked
  Hash.Mode........: 18200 (Kerberos 5, AS-REP Pre-Auth etype 23)
  Hash.Target......: hashes.txt
  Recovered........: 1/1 (100.00%) Digests
  user:password123
created_at: '2020-03-17T04:34:06.715518+00:00'
updated_at: '2023-05-25T19:59:26.357810+00:00'
platforms:
  - Linux
tags:
  - cracking
  - hashcat
verified: true
validated: true
---

# hashcat-brute-force-as-rep-hashes

## Command

```bash
hashcat -m 18200 $_HASH_FILE.txt $_WORDLIST.txt -O
```

## Description

Cracks Kerberos AS-REP hashes using dictionary attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m 18200 | AS-REP mode | Yes |
| $_HASH_FILE.txt | Input hashes | Yes |
| $_WORDLIST.txt | Dictionary file | Yes |
| -O | Optimized kernels | No |

## Examples

### Basic Usage

```bash
hashcat -m 18200 asrep.txt rockyou.txt
```

## Expected Output

Cracked passwords displayed.

## Related

- [[procedures/Brute-Force-Password-Hashes-with-Hashcat]]
- [[tools/Hashcat]]
