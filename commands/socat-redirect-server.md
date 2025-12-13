---
data: >-
  socat -v -d -d TCP-LISTEN:443,crlf,reuseaddr,fork 'SYSTEM:/bin/echo "HTTP/1.1
  302 Found";/bin/echo "Content-Length: 0";/bin/echo "Location:
  https://pqp.mx:8443";/bin/echo;/bin/echo'
tags:
  - redirect
  - server
type: command
executor: bash
platforms:
  - Linux
id: 2f238b22-2193-4f1a-815c-a0d3e802f7f8
created_at: '2025-12-13T09:01:17.560Z'
updated_at: '2025-12-13T09:01:17.560Z'
verified: false
validated: true
submitted: true
---
# Socat Redirect Server

## Command

```bash
socat -v -d -d TCP-LISTEN:443,crlf,reuseaddr,fork 'SYSTEM:/bin/echo "HTTP/1.1 302 Found";/bin/echo "Content-Length: 0";/bin/echo "Location: https://pqp.mx:8443";/bin/echo;/bin/echo'
```

## Description

Sets up a TCP listener on port 443 that responds to incoming connections with an HTTP 302 redirect to a specified location, used in redirect exploitation chains.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | No |
| `-d -d` | Double debug mode | No |
| `TCP-LISTEN:443` | Listen on TCP port 443 | Yes |
| `crlf` | Use CRLF line endings | Yes |
| `reuseaddr` | Reuse address for binding | Yes |
| `fork` | Fork after connection | Yes |
| `SYSTEM:...` | Execute shell commands to send HTTP response | Yes |

## Examples

### Basic Usage

```bash
socat -v -d -d TCP-LISTEN:443,crlf,reuseaddr,fork 'SYSTEM:/bin/echo "HTTP/1.1 302 Found";/bin/echo "Content-Length: 0";/bin/echo "Location: https://pqp.mx:8443";/bin/echo;/bin/echo'
```

### Advanced Usage

```bash
socat -v -d -d TCP-LISTEN:80,crlf,reuseaddr,fork 'SYSTEM:/bin/echo "HTTP/1.1 302 Found";/bin/echo "Location: https://example.com";/bin/echo'
```

## Expected Output

Incoming connections receive a 302 redirect response, leading to further redirect to the specified location. Verbose logs show connection details.

## Related

- [[procedures/Set-Up-Redirect-Server]]
- [[tools/socat]]
