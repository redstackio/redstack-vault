---
id: cmd-ssh-login-001
data: ssh operator@192.168.1.1
tags:
  - access
  - ssh
type: command
output: 'operator@edgeos:~$'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:27.916Z'
verified: false
validated: true
submitted: true
---
# ssh-login

## Command

```bash
ssh operator@192.168.1.1
```

## Description

Connects to EdgeOS via SSH as operator.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `operator@ip` | User and host | Yes |

## Examples

### Basic Usage

```bash
ssh operator@192.168.1.1
```

### Advanced Usage

```bash
ssh -i key.pem operator@192.168.1.1
```

## Expected Output

Shell prompt after password.

## Related

- [[commands/id-verify]]
