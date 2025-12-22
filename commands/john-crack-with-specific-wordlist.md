---
type: command
executor: bash
data: john --wordlist=$_WORDLIST_PATH $_HASH_FILE
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - hash-cracking
  - john
  - dictionary-attack
verified: true
validated: true
---

# john-crack-with-specific-wordlist

## Command

```bash
john --wordlist=$_WORDLIST_PATH $_HASH_FILE
```

## Description

Performs a dictionary attack using a specified wordlist to guess passwords against the hashes in the file. Ideal for targeting known common passwords or custom lists derived from reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --wordlist | Flag to specify the wordlist file | Yes |
| $_WORDLIST_PATH | Path to the wordlist (e.g., /usr/share/wordlists/rockyou.txt) | Yes |
| $_HASH_FILE | Path to the hash file | Yes |

## Examples

### Basic Usage

```bash
john --wordlist=rockyou.txt hashes.txt
```

### Advanced Usage

```bash
john --wordlist=custom.txt --fork=4 hashes.txt
```

## Expected Output

Loaded 1 password hash (NTLM [MD4 128/128 SSE2 4x3])
PROGRESS (wordlist:/path/to/rockyou.txt) [912/1000000]
password (user)
```

## Related

- [[procedures/Crack-Password-Hashes-with-John-the-Ripper]]
- [[tools/John-the-Ripper]]
