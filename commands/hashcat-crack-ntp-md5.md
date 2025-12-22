---
type: command
executor: bash
data: hashcat -m 31300 ntp-hashes.txt $_WORDLIST
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - cracking
  - ntp
  - md5
verified: true
validated: true
---

# hashcat-crack-ntp-md5

## Command

```bash
hashcat -m 31300 ntp-hashes.txt $_WORDLIST
```

## Description

This command cracks NTP MD5 authentication hashes extracted from a server using Hashcat's mode 31300. It performs a dictionary attack to recover the plaintext symmetric key, enabling NTP packet forgery for time manipulation. Ideal for offline analysis after hash extraction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m 31300 | Hash mode for NTP MD5 authentication | Yes |
| ntp-hashes.txt | File containing extracted hashes | Yes |
| $_WORDLIST | Path to dictionary file for cracking | Yes |

## Examples

### Basic Usage

```bash
hashcat -m 31300 ntp-hashes.txt /usr/share/wordlists/rockyou.txt
```

### With Rules for Better Coverage

```bash
hashcat -m 31300 ntp-hashes.txt /usr/share/wordlists/rockyou.txt -r rules/best64.rule
```

## Expected Output

Progress status and cracked results, e.g.:

ntp-md5::10.0.0.42:123:password123

Recovered: 1/1 (100%) hashes, plaintext: password123

## Related

- [[procedures/Timeroasting-NTP-Servers-to-Crack-Authentication-Keys]]
- [[commands/timeroast-extract-ntp-hashes]]
