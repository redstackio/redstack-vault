---
type: command
executor: bash
data: ssh -i $_KEY_FILE $_USERNAME@$_EC2_HOSTNAME
tags:
  - ssh
  - ec2
platforms:
  - Linux
verified: true
validated: true
---

# ssh-connect-to-ec2-instance

## Command

```bash
ssh -i $_KEY_FILE $_USERNAME@$_EC2_HOSTNAME
```

## Description

Establishes a secure shell connection to an EC2 instance using a private key for authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i $_KEY_FILE | Path to private key file | Yes |
| $_USERNAME | Username (e.g., ubuntu, ec2-user) | Yes |
| $_EC2_HOSTNAME | EC2 public or private DNS/IP | Yes |

## Examples

### Basic Usage

```bash
ssh -i mykey.pem ubuntu@ec2-12-34-56-78.compute-1.amazonaws.com
```

### Advanced Usage

With verbose:

```bash
ssh -i mykey.pem -v ubuntu@ec2-12-34-56-78.compute-1.amazonaws.com
```

## Expected Output

Interactive shell prompt:

`ubuntu@ip-172-31-0-1:~$ `

## Related

- [[commands/chmod-secure-private-key]]
- [[procedures/AWS-Extract-EBS-Backup-to-EC2-Instance]]
