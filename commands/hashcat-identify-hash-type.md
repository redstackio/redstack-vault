---
id: new-uuid-for-this
name: hashcat-identify-hash-type
type: command
executor: bash
data: hashcat --example-hashes | grep -i $_HASH_PREFIX
output: >-
  Example output showing matching modes, e.g., $axcrypt_sha1$...: Mode 13300
  (AxCrypt).
created_at: '2023-01-01T00:00:00.000000+00:00'
updated_at: '2023-01-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - hashing
  - identification
verified: true
validated: true
---

# hashcat-identify-hash-type

## Command

```bash
hashcat --example-hashes | grep -i $_HASH_PREFIX
```

## Description

Queries Hashcat's built-in example hashes to identify the type based on prefix or format.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_HASH_PREFIX | Prefix like $ntlm$ or axcrypt_sha1 | Yes |
| --example-hashes | Display example hashes | Built-in |

## Examples

### Basic Usage

```bash
hashcat --example-hashes | grep axcrypt
```

## Expected Output

Lines matching the prefix with mode numbers.

## Related

- [[procedures/identify-password-hash-hashcat]]
