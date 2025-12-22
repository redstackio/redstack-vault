---
type: command
executor: bash
data: john --format=netntlm $_HASH_FILE --wordlist=$_WORDLIST
output: null
created_at: '2023-04-06T03:56:05.188182+00:00'
updated_at: '2023-04-10T20:35:59.633859+00:00'
platforms:
  - Linux
tags:
  - cracking
  - ntlm
verified: true
validated: true
---

# john-crack-netntlm

## Command

```bash
john --format=netntlm $_HASH_FILE --wordlist=$_WORDLIST
```

## Description

Cracks Net-NTLMv1 hashes using John the Ripper with dictionary attack. Specify format for NetNTLM support; use --incremental for brute-force.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --format=netntlm | Hash type for Net-NTLMv1 | Yes |
| $_HASH_FILE | Path to formatted hash file | Yes |
| --wordlist=$_WORDLIST | Path to dictionary file | No (for dict attack) |

## Examples

### Dictionary Attack

```bash
john --format=netntlm hashes.txt --wordlist=rockyou.txt
```

### Brute Force

```bash
john --format=netntlm hashes.txt --incremental
```

## Expected Output

`Loaded 1 password hash` then progress; cracked: `password123 (user)` upon success.

## Related

- [[procedures/Capture-and-Crack-Net-NTLMv1-Hashes]]
- [[tools/John-the-Ripper]]
