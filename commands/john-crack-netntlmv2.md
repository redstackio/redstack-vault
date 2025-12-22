---
type: command
executor: bash
data: john --format=netntlmv2 $_HASH_FILE --wordlist=$_WORDLIST
tags:
  - cracking
  - ntlm
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# john-crack-netntlmv2

## Command

```bash
john --format=netntlmv2 $_HASH_FILE --wordlist=$_WORDLIST
```

## Description

Cracks Net-NTLMv2 hashes using John the Ripper with a dictionary attack to recover plaintext passwords.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --format=netntlmv2 | Specifies Net-NTLMv2 hash format | Yes |
| $_HASH_FILE | Path to file containing captured hashes | Yes |
| --wordlist | Uses dictionary file for attack | No |
| $_WORDLIST | Path to wordlist (e.g., rockyou.txt) | No |

## Examples

### Basic Usage

```bash
john --format=netntlmv2 hashes.txt --wordlist=rockyou.txt
```

### Advanced Usage

```bash
john --format=netntlmv2 hashes.txt --wordlist=rockyou.txt --rules
```

## Expected Output

```
Loaded 1 password hash (netntlmv2, NTLMv2 [LM NetBIOS Sids 48/96])
Press 'q' or Ctrl-C to abort, almost any other key for status
password         (user)
1g 0:00:00:00 DONE (2023-01-01 12:00) 100g/s 1234p/s 1234c/s 1234C/s
```
Displays cracked password on success.

## Related

- [[procedures/Net-NTLMv2-Hash-Capture-and-Cracking]]
- [[tools/John-the-Ripper]]
