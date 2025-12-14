---
id: cmd-nc-ssrf-001
data: nc -l 81
tags:
  - network
  - listen
  - ssrf
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.537Z'
verified: false
validated: true
submitted: true
---
# nc-listen-for-ssrf

## Command

```bash
nc -l 81
```

## Description

This command uses netcat to listen for incoming connections on port 81, capturing SSRF requests from the target server when processing malicious SVGs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Listen mode | Yes |
| `81` | Port to listen on | Yes |

## Examples

### Basic Usage

```bash
nc -l 81
```

### Advanced Usage

```bash
nc -l -p 81 -v
```
(Add -v for verbose output.)

## Expected Output

Connection from server IP when SVG with external href is processed, e.g., "Connection from 10.0.0.1:12345 received!"

## Related

- [[Related Procedure|procedures/Exploit-XXE-for-SSRF-via-External-Resource-Fetch]]
