---
type: command
executor: bash
data: ssh -o ConnectTimeout=10 $_USER@$_PIVOT_HOST
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Unix
  - macOS
tags:
  - ssh
  - testing
verified: true
validated: true
---

# ssh-test-connection

## Command

```bash
ssh -o ConnectTimeout=10 $_USER@$_PIVOT_HOST
```

## Description

This command tests SSH connectivity to a pivot host with a 10-second timeout, verifying credentials and network access before setting up a tunnel. Use it as a prerequisite step to avoid tunnel failures due to authentication issues.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USER | Username for SSH authentication | Yes |
| $_PIVOT_HOST | IP address or hostname of the pivot server | Yes |
| -o ConnectTimeout=10 | Set connection timeout to 10 seconds | No (default is longer) |

## Examples

### Basic Usage

```bash
ssh -o ConnectTimeout=10 user@192.168.1.100
```

### Advanced Usage

```bash
ssh -o ConnectTimeout=10 -i /path/to/key user@host.example.com
```

## Expected Output

Successful connection shows:
```
user@192.168.1.100's password: 
Last login: ... from ...
```
Followed by a shell prompt. Failure: "Connection timed out" or "Permission denied".

## Related

- [[procedures/SSH-Local-Port-Forwarding]]
- [[commands/ssh-create-local-port-forward]]
