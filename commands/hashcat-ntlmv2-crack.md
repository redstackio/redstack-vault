---
id: cmd-uuid-2
data: hashcat -m 5600 captured_hashes.txt /usr/share/wordlists/rockyou.txt -O
tags:
  - cracking
  - ntlmv2
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.057Z'
verified: false
validated: true
submitted: true
---
# hashcat-ntlmv2-crack

## Command

```bash
hashcat -m 5600 captured_hashes.txt /usr/share/wordlists/rockyou.txt -O
```

## Description

Cracks NTLMv2 hashes offline using Hashcat, recovering plaintext passwords from captured SMB auth data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m 5600` | Hash mode for NTLMv2 | Yes |
| `captured_hashes.txt` | Input file with hashes | Yes |
| `/usr/share/wordlists/rockyou.txt` | Wordlist path | Yes |
| `-O` | Optimized kernel | No |

## Examples

### Basic Usage

```bash
hashcat -m 5600 hashes.txt rockyou.txt
```

### Advanced Usage

```bash
hashcat -m 5600 -a 3 hashes.txt ?l?l?l?l?d?d?d?d
```

## Expected Output

Cracked passwords displayed as 'username:password' if successful, or session resume info.

## Related

- [[Related Procedure: Analyze-Captured-NTLMv2-Hashes]]
