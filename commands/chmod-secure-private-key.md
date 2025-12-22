---
type: command
executor: bash
data: chmod 400 $_KEY_FILE
tags:
  - ssh
  - security
platforms:
  - Linux
verified: true
validated: true
---

# chmod-secure-private-key

## Command

```bash
chmod 400 $_KEY_FILE
```

## Description

Sets read-only permissions for the owner on a private SSH key file, preventing unauthorized access and satisfying SSH client requirements for secure key usage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_KEY_FILE | Path to the PEM private key file (e.g., mykey.pem) | Yes |

## Examples

### Basic Usage

```bash
chmod 400 mykey.pem
```

### Advanced Usage

For a key in a specific directory:

```bash
chmod 400 /path/to/keys/ec2-key.pem
```

## Expected Output

No output on success; the file permissions change to 400 (drwx------). Verify with `ls -l $_KEY_FILE` showing `-r--------`.

## Related

- [[commands/ssh-connect-to-ec2-instance]]
- [[procedures/AWS-Extract-EBS-Backup-to-EC2-Instance]]
