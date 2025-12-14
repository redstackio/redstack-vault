---
id: cmd-nc-listener
data: nc -l 1337
tags:
  - listener
  - tcp
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.063Z'
verified: false
validated: true
submitted: true
---
# nc-listener

## Command

```bash
nc -l 1337
```

## Description

Netcat in listen mode to capture incoming TCP connections from SSRF, e.g., when appending query params to force Ruby refetch.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l | Listen mode | Yes |
| 1337 | Port to bind | Yes |

## Examples

### Basic Usage

```bash
nc -l 1337
```

### Advanced Usage

```bash
nc -l -p 1337 -v
```
(Verbose output)

## Expected Output

Connection from [target IP] 12345
GET / HTTP/1.1
Host: 192.166.218.53:1337
User-Agent: Ruby

## Related

- [[procedures/Verify-SSRF-Exploitation-in-Logs]]
- [[tools/Netcat]]
