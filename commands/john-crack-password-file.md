---
type: command
executor: bash
data: john $_HASH_FILE
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - hash-cracking
  - john
verified: true
validated: true
---

# john-crack-password-file

## Command

```bash
john $_HASH_FILE
```

## Description

This command runs John the Ripper in default mode to crack passwords from a hash file using built-in strategies like single crack and incremental mode. Use it for initial attempts on captured hashes without custom wordlists.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_HASH_FILE | Path to the file containing password hashes (e.g., hashes.txt) | Yes |

## Examples

### Basic Usage

```bash
john hashes.txt
```

### Advanced Usage

```bash
john --format=sha512crypt hashes.txt
```

## Expected Output

Loaded 5 password hashes with no different salts
Remaining 3 password hashes
Guesses: 123456 → user1
```

## Related

- [[procedures/Crack-Password-Hashes-with-John-the-Ripper]]
- [[tools/John-the-Ripper]]
