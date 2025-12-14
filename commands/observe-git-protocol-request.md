---
id: cmd-observe-git-request-001
data: tail -f /var/log/http-server.log | grep 'git-upload-pack'
tags:
  - log
  - ssrf
  - git
type: command
output: >-
  40.84.0.225 - - [01/Oct/2023:00:00:00] "GET /info/refs?service=git-upload-pack
  HTTP/1.1" 404 123
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.096Z'
verified: false
validated: true
submitted: true
---
# observe-git-protocol-request

## Command

```bash
tail -f /var/log/http-server.log | grep 'git-upload-pack'
```

## Description

Monitors HTTP server logs in real-time for Git protocol requests indicative of SSRF in GitLab imports, filtering for the service parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f` | Follow log file continuously | Yes |
| `/var/log/http-server.log` | Path to access log | Yes |
| `grep 'git-upload-pack'` | Filter for Git service | Yes |

## Examples

### Basic Usage

```bash
tail -f access.log | grep 'git-upload-pack'
```

### Advanced Usage

```bash
tail -f access.log | grep 'git-upload-pack' | awk '{print $1}'
```

## Expected Output

Filtered log lines showing GET requests with service=git-upload-pack, including source IP like GitLab's 40.84.0.225 and 404 status.

## Related

- [[Related Procedure|procedures/Verify-SSRF-via-Access-Logs]]
