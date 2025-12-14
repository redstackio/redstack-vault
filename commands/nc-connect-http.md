---
id: cmd-nc-connect
type: command
executor: bash
data: nc localhost 80
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.873Z'
platforms:
  - Linux
  - macOS
tags:
  - network
  - http
verified: false
validated: true
submitted: true
---

# nc-connect-http

## Command

```bash
nc localhost 80
```

## Description

Establishes a raw TCP connection to the target host on port 80 using Netcat, allowing manual input of HTTP requests for testing vulnerabilities like chunked encoding flaws.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| localhost | Target hostname or IP | Yes |
| 80 | Target port for HTTP | Yes |

## Examples

### Basic Usage

```bash
nc localhost 80
```

### Advanced Usage

```bash
nc 192.168.1.100 80
```

## Expected Output

Opens an interactive session; type HTTP requests and receive server responses, e.g., connection prompt without errors.

## Related

- [[commands/send-chunked-xss-request]]
- [[procedures/Send-Crafted-Chunked-POST-Request-with-XSS-Payload]]
