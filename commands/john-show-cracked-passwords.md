---
type: command
executor: bash
data: john --show $_HASH_FILE
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - hash-cracking
  - john
  - results
verified: true
validated: true
---

# john-show-cracked-passwords

## Command

```bash
john --show $_HASH_FILE
```

## Description

Displays all cracked passwords from a previous John session without re-cracking. Useful for reviewing results after interruption or completion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --show | Flag to display cracked passwords | Yes |
| $_HASH_FILE | Path to the original hash file | Yes |

## Examples

### Basic Usage

```bash
john --show hashes.txt
```

### Advanced Usage

```bash
john --show --format=ntlm hashes.txt
```

## Expected Output

user1:password123 (hash1)
user2:letmein (hash2)
3 password hashes cracked, 2 left uncracked.
```

## Related

- [[procedures/Crack-Password-Hashes-with-John-the-Ripper]]
- [[tools/John-the-Ripper]]
