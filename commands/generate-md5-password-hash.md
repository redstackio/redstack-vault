---
type: command
executor: bash
data: openssl passwd -1 -salt $_SALT $_PASSWORD
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - hashing
  - privesc
verified: true
validated: true
---

# generate-md5-password-hash

## Command

```bash
openssl passwd -1 -salt $_SALT $_PASSWORD
```

## Description

Generates an MD5 hashed password with a specified salt for use in /etc/passwd entries during account creation in privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -1 | Use MD5 algorithm | Yes |
| -salt $_SALT | Salt value (e.g., 'hacker') | Yes |
| $_PASSWORD | Plaintext password to hash | Yes |

## Examples

### Basic Usage

```bash
openssl passwd -1 -salt hacker hacker
```

### Advanced Usage

```bash
openssl passwd -1 -salt mysalt mypass
```
For a custom password.

## Expected Output

```
$1$hacker$abc123def456ghi789
```
Copy this hash for use in passwd entry.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Writable-etc-passwd]]
- [[commands/add-user-to-etc-passwd-with-hash]]
