---
id: cmd-hashcat-brute
data: >-
  hashcat -m 1000 -a 3 extracted_hash.txt ?l?l?l?l?d?d --increment
  --increment-min=4 --increment-max=8
tags:
  - cracking
  - brute-force
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.727Z'
verified: false
validated: true
submitted: true
---
# hashcat-brute

## Command

```bash
hashcat -m 1000 -a 3 extracted_hash.txt ?l?l?l?l?d?d --increment --increment-min=4 --increment-max=8
```

## Description

This command performs a mask-based brute-force attack using Hashcat on a PBKDF2-derived hash (mode 1000, common for app passwords), tailored to the biased generation in Rocket.Chat E2EE passwords. It increments length from 4-8 characters with lowercase and digit focus, exploiting reduced entropy.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m 1000` | Hash mode for PBKDF2-HMAC-SHA1 | Yes |
| `-a 3` | Attack mode: mask | Yes |
| `extracted_hash.txt` | File containing the target hash | Yes |
| `?l?l?l?l?d?d` | Mask: 4 lowercase + 2 digits (customize per bias) | Yes |
| `--increment` | Enable length increment | Yes |
| `--increment-min=4` | Min length | No |
| `--increment-max=8` | Max length | No |

## Examples

### Basic Usage

```bash
hashcat -m 1000 -a 3 hash.txt ?l?l?l?l
```

### Advanced Usage

```bash
hashcat -m 1000 -a 3 hash.txt ?l?l?l?l?d?d -w 3 -O
```

(Adds high workload profile and optimization for GPU.)

## Expected Output

On success: "Cracked: pass1234" with session stats; failure shows progress percentage without recovery.

## Related

- [[Related Procedure|Brute-Force-E2EE-Password]]
