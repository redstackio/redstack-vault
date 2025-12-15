---
id: cmd-ssh-vps
data: ssh ███████
tags:
  - ssh
  - access
type: command
output: Successful SSH session login
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.599Z'
verified: false
validated: true
submitted: true
---
# ssh-login-to-vps

## Command

```bash
ssh ███████
```

## Description

Initiates an SSH connection to the attacker's redacted VPS hostname to access the shell for exploit setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hostname | Redacted VPS hostname (e.g., user@ip-or-domain) | Yes |

## Examples

### Basic Usage

```bash
ssh ███████
```

### Advanced Usage

```bash
ssh -i key.pem ███████
```

## Expected Output

Authentication successful, followed by shell prompt: `user@hostname:~$`.

## Related

- [[procedures/SSH-Login-to-Attacker-VPS]]
