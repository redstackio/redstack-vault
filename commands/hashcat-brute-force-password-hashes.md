---
id: d0a77568-8751-435e-a7e7-102256247007
name: hashcat-brute-force-password-hashes
type: command
executor: bash
data: hashcat -m $_MODE $_HASH_FILE $_WORDLIST
output: |-
  root@kali:~# hashcat -m 1800 test /usr/share/wordlists/rockyou.txt
  ... (cracked output) ...
created_at: '2020-01-20T20:42:02.727182+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Windows
tags:
  - cracking
verified: true
validated: true
---

# hashcat-brute-force-password-hashes

## Command

```bash
hashcat -m $_MODE $_HASH_FILE $_WORDLIST
```

## Description

Cracks hashes using dictionary attack in specified mode.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m $_MODE | Hash mode (e.g., 18200) | Yes |
| $_HASH_FILE | File with hashes | Yes |
| $_WORDLIST | Password dictionary | Yes |

## Examples

### Basic Usage

```bash
hashcat -m 18200 hashes.txt rockyou.txt
```

### With Rules

```bash
hashcat -m 18200 hashes.txt rockyou.txt -r rules/best64.rule
```

## Expected Output

... Session Cracked: username:password ...

## Related

- [[procedures/Brute-Force-Password-Hashes-with-Hashcat]]
