---
id: cmd-nc-connect-001
data: nc -v <target_ip> 4786
tags:
  - recon
  - probe
type: command
output: null
executor: bash
platforms:
  - Linux
  - Network
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.339Z'
verified: false
validated: true
submitted: true
---
# nc-connect

## Command

```bash
nc -v <target_ip> 4786
```

## Description

Attempts a verbose connection to the SMI port to verify responsiveness and lack of authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | Yes |
| `<target_ip>` | Target IP | Yes |
| `4786` | Port number | Yes |

## Examples

### Basic Usage

```bash
nc -v 192.168.1.100 4786
```

### Advanced Usage

```bash
nc -v -w 5 192.168.1.100 4786
```

## Expected Output

Connection to 192.168.1.100 4786 port [tcp/*] succeeded!

## Related

- [[Related Procedure: Discover-Exposed-Cisco-SMI-Service]]
