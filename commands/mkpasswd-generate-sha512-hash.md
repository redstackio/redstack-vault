---
type: command
executor: bash
data: mkpasswd -m sha-512 -S $_SALT $_PASSWORD
tags:
  - cryptography
  - password-hashing
platforms:
  - Linux
verified: true
validated: true
---

# mkpasswd-generate-sha512-hash

## Command

```bash
mkpasswd -m sha-512 -S $_SALT $_PASSWORD
```

## Description

This command generates a SHA-512 hashed password using the specified salt and plaintext password. It is useful for creating realistic password hashes for testing authentication systems, simulating /etc/shadow entries, or preparing data for offline cracking exercises in red team operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m sha-512 | Specifies the hashing method as SHA-512 (sha512crypt) | Yes |
| -S $_SALT | The salt string to use for hashing (typically 8-16 random characters) | Yes |
| $_PASSWORD | The plaintext password to be hashed | Yes |

## Examples

### Basic Usage

```bash
mkpasswd -m sha-512 -S 16bytesXX16bytes Thisisyourpassword
```

### Advanced Usage

```bash
mkpasswd -m sha-512 -S customsalt -R 10000 strongpassword
```

This adds 10,000 hashing rounds for a more secure hash.

## Expected Output

Description of what output to expect when the command runs successfully.

The command outputs a single line with the generated hash in the standard crypt format, prefixed with $6$ for SHA-512.

```
$6$16bytesXX16bytes$FXuYP0OI7qYB3K6u6.91Blr7rtvjLZmpcuAWuWVnTj4G2nVGny6k5yzaDbV3iQCwoSDMGgXePvFxddnxYkpa5/
```

## Related

- [[tools/mkpasswd]]
- [[commands/mkpasswd-generate-sha256-hash]] (for SHA-256 variant)
