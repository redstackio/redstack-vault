---
type: command
executor: bash
data: john --wordlist=$_WORDLIST_PATH --rules=$_RULESET $_HASH_FILE
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - hash-cracking
  - john
  - rules
verified: true
validated: true
---

# john-crack-with-wordlist-and-rules

## Command

```bash
john --wordlist=$_WORDLIST_PATH --rules=$_RULESET $_HASH_FILE
```

## Description

Runs a dictionary attack enhanced with rules to mutate words (e.g., append '1', toggle case), increasing coverage for patterned passwords without full brute force.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --wordlist | Flag for wordlist input | Yes |
| $_WORDLIST_PATH | Path to wordlist file | Yes |
| --rules | Flag for rule set (e.g., Jumbo for advanced mutations) | Yes |
| $_RULESET | Name of the ruleset (built-in or custom) | Yes |
| $_HASH_FILE | Path to hash file | Yes |

## Examples

### Basic Usage

```bash
john --wordlist=rockyou.txt --rules=Jumbo hashes.txt
```

### Advanced Usage

```bash
john --wordlist=rockyou.txt --rules=Best64 --incremental hashes.txt
```

## Expected Output

Loaded 2 password hashes...
Using rules: Jumbo (advanced mutations)
Guesses: Password1 → admin
```

## Related

- [[procedures/Crack-Password-Hashes-with-John-the-Ripper]]
- [[tools/John-the-Ripper]]
