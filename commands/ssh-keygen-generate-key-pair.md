---
id: f846776d-654e-40c3-ba33-316a0297d86c
name: ssh-keygen-generate-key-pair
type: command
executor: bash
data: ssh-keygen -t rsa -b 2048 -f ~/.ssh/aws_persistence_key -N ""
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - ssh
  - key-generation
  - persistence
verified: true
validated: true
---

# ssh-keygen-generate-key-pair

## Command

```bash
ssh-keygen -t rsa -b 2048 -f ~/.ssh/aws_persistence_key -N ""
```

## Description

Generates a new 2048-bit RSA SSH key pair without a passphrase, saving the private key to ~/.ssh/aws_persistence_key and public key to ~/.ssh/aws_persistence_key.pub. Use this for creating persistent access keys in scenarios like AWS EC2 persistence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t rsa` | Specifies RSA key type | Yes |
| `-b 2048` | Key size in bits (2048 for security) | Yes |
| `-f ~/.ssh/aws_persistence_key` | Output file path for the key pair | Yes |
| `-N ""` | No passphrase (empty string); use a passphrase for added security | No |

## Examples

### Basic Usage

```bash
ssh-keygen -t rsa -b 2048 -f ~/.ssh/mykey
```

### With Passphrase

```bash
ssh-keygen -t rsa -b 2048 -f ~/.ssh/mykey -N "mypassword"
```

## Expected Output

Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/aws_persistence_key
Your public key has been saved in /home/user/.ssh/aws_persistence_key.pub
The key fingerprint is:
SHA256:abc123... user@local
The key's randomart image is:
+---[RSA 2048]----+
| ... |
+----[SHA256]-----+

## Related

- [[procedures/aws-ssh-key-persistence]]
- [[tools/OpenSSH]]
