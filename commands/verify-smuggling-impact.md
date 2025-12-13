---
data: 'curl -v http://target.com -d @smuggling-payload.txt'
tags:
  - http
  - verification
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: f1b94767-aa9d-4e0d-b204-77b654ae46b0
created_at: '2025-12-13T09:01:17.711Z'
updated_at: '2025-12-13T09:01:17.711Z'
verified: false
validated: true
submitted: true
---
# Verify Smuggling Impact

## Command

```bash
curl -v http://target.com -d @smuggling-payload.txt
```

## Description

Sends a file-based payload to verify if HTTP Request Smuggling was successful by observing server behavior.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | No |
| `-d @file` | Send data from file | Yes |
| `http://target.com` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl http://example.com -d @payload.txt
```

### Advanced Usage

```bash
curl -v -H "Content-Type: text/plain" http://example.com -d @payload.txt
```

## Expected Output

Response indicating smuggled request processed, such as unauthorized access.

## Related

- [[procedures/Execute-Request-Smuggling-Attack]]
