---
type: command
executor: bash
data: ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_persist -N ""
tags:
  - ssh
  - key-generation
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# generate-ssh-key-pair

## Command

```bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_persist -N ""
```

## Description

Generates a new RSA SSH key pair for persistence purposes, specifying a custom filename to avoid overwriting default keys. The empty passphrase (-N "") allows non-interactive use.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t rsa | Key type (RSA) | Yes |
| -b 4096 | Key length in bits | Yes |
| -f ~/.ssh/id_persist | Output file path (base name for .pub too) | Yes |
| -N "" | Passphrase (empty for no passphrase) | Yes |

## Examples

### Basic Usage

```bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_persist -N ""
```

### Advanced Usage

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed_persist -N ""
```
(Uses Ed25519 for faster generation on modern systems.)

## Expected Output

Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user/.ssh/id_persist
Your public key has been saved in /home/user/.ssh/id_persist.pub
The key fingerprint is:
SHA256:abc123... user@attacker
The key's randomart image is:
+---[RSA 4096]----+
| ... |
+----[SHA256]-----+

## Related

- [[procedures/SSH-Key-Persistence]]
- [[commands/add-ssh-public-key-via-copy-id]]
