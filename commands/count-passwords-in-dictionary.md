---
id: cmd-count-passwords
data: cat 10k_most_common.txt | wc -l
tags:
  - wordlist
  - verification
type: command
output: '10001'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.774Z'
verified: false
validated: true
submitted: true
---
# count-passwords-in-dictionary

## Command

```bash
cat 10k_most_common.txt | wc -l
```

## Description

Counts the number of lines (passwords) in a dictionary file to verify its size before using in brute-force attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 10k_most_common.txt | Path to the password file | Yes |

## Examples

### Basic Usage

```bash
cat 10k_most_common.txt | wc -l
```

### Advanced Usage

For any file:

```bash
cat passwords.txt | wc -l
```

## Expected Output

10001 (indicating 10,001 passwords after appending test entry).

## Related

- [[commands/view-end-of-password-list]]
- [[procedures/Prepare-Password-Dictionary]]
