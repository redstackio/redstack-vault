---
data: nc -l 8081
tags:
  - netcat
  - listen
type: command
output: null
executor: bash
platforms:
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.553Z'
id: 8b3728ec-e8e2-4f84-90b4-6d1708439941
verified: false
validated: true
submitted: true
---
# nc-listen-port

## Command

```bash
nc -l 8081
```

## Description

Starts a netcat listener on TCP port 8081 to capture incoming connections and display raw data, ideal for intercepting HTTP requests and headers in security testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Listen mode for incoming connections | Yes |
| `8081` | Port to bind to | Yes |

## Examples

### Basic Usage

```bash
nc -l 8081
```

### Advanced Usage

```bash
nc -l -p 8081 -v  # Verbose mode
```

## Expected Output

Awaits connection: no immediate output until data received, then dumps full TCP stream (e.g., HTTP headers and body).

## Related

- [[commands/curl-with-proxy-auth-redirect]]
- [[procedures/Capture-Requests-with-Netcat-Listener]]
