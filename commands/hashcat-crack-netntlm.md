---
type: command
executor: bash
data: hashcat -m 5500 -a 0 $_HASH_FILE $_WORDLIST
output: null
created_at: '2023-04-06T03:56:05.188281+00:00'
updated_at: '2023-04-10T20:35:59.633859+00:00'
platforms:
  - Linux
tags:
  - cracking
  - ntlm
verified: true
validated: true
---

# hashcat-crack-netntlm

## Command

```bash
hashcat -m 5500 -a 0 $_HASH_FILE $_WORDLIST
```

## Description

Cracks Net-NTLMv1 hashes using Hashcat in dictionary mode (-a 0). Mode 5500 is for NetNTLMv1; switch to -a 3 for brute-force masks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m 5500 | Net-NTLMv1 hash mode | Yes |
| -a 0 | Dictionary attack mode | Yes |
| $_HASH_FILE | Path to formatted hash(es) | Yes |
| $_WORDLIST | Path to wordlist | Yes |

## Examples

### Dictionary Attack

```bash
hashcat -m 5500 -a 0 hashes.txt rockyou.txt
```

### Brute Force

```bash
hashcat -m 5500 -a 3 hashes.txt ?l?l?l?l?d?d
```

## Expected Output

Progress bar with speed; `Cracked: password123` in potfile upon success.

## Related

- [[procedures/Capture-and-Crack-Net-NTLMv1-Hashes]]
- [[tools/Hashcat]]
