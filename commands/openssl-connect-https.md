---
id: cmd-openssl-connect
data: 'openssl s_client -connect drive.uber.com:443 -quiet'
tags:
  - https
  - connect
  - network
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.953Z'
verified: false
validated: true
submitted: true
---
# openssl-connect-https

## Command

```bash
openssl s_client -connect drive.uber.com:443 -quiet
```

## Description

Establishes a quiet HTTPS connection to a target server for sending raw HTTP requests, suppressing handshake noise to focus on request/response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -connect | Host:port to connect (e.g., drive.uber.com:443) | Yes |
| -quiet | Suppresses certificate and connection verbosity | No |

## Examples

### Basic Usage

```bash
openssl s_client -connect example.com:443 -quiet
```

### Advanced Usage

Pipe input for requests: echo "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n" | openssl s_client -connect example.com:443 -quiet

## Expected Output

Open socket connection; ready for stdin input of HTTP requests, with response echoed to stdout.

## Related

- [[commands/perl-inject-xss-http-request]]
- [[procedures/Inject-XSS-Payload-via-Malformed-HTTP-Request]]
