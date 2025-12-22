---
id: 8d4b8df0-6846-4888-9305-86d99216b208
name: john-convert-sam-to-nt-format
type: command
executor: bash
data: john --format=NT /root/sam.txt
output: null
created_at: '2023-04-06T03:56:28.805858+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - cracking
  - hashes
verified: true
validated: true
---

# john-convert-sam-to-nt-format

## Command

```bash
john --format=NT /root/sam.txt
```

## Description

This command loads NTLM hashes from a pwdump or samdump output file into John the Ripper for cracking in NT format, attempting to recover plaintext passwords using dictionary attacks or incremental modes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--format=NT` | Specifies NTLM hash format for loading | Yes |
| `/root/sam.txt` | Path to the hash file containing NTLM hashes | Yes |

## Examples

### Basic Usage

```bash
john --format=NT /root/sam.txt
```

### Advanced Usage

```bash
john --format=NT --wordlist=/usr/share/wordlists/rockyou.txt /root/sam.txt
```

## Expected Output

Loaded 5 password hashes with no different salts (NT [MD4 128/128 SSE2 4x3])
Remaining 5 password hashes

Guesses: 12345 (progress updates during cracking)

Recovered passwords: password123 (if successful).

## Related

- [[procedures/Windows-SAM-and-SYSTEM-Hash-Extraction]]
- [[tools/john-the-ripper]]
