---
id: cmd-nc-listen-verbose
data: nc -lvv 6655
tags:
  - listener
  - tcp
  - ssrf-verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.438Z'
verified: false
validated: true
submitted: true
---
# nc-listen-verbose

## Command

```bash
nc -lvv 6655
```

## Description

Listens for incoming TCP connections on a specified port in verbose mode to capture SSRF-triggered requests from vulnerable applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Listen mode for incoming connections | Yes |
| `-v` | Verbose output (connection details) | Yes |
| `-v` (second) | Additional verbosity (data transfer) | No |
| `6655` | Port to listen on (e.g., 6655, 6666) | Yes |

## Examples

### Basic Usage

```bash
nc -lvv 6655
```

### Advanced Usage

Listen on multiple ports sequentially or use scripts for automation.

```bash
nc -lvv 5555  # For HTTP variant
```

## Expected Output

'Listening on [0.0.0.0] (family 0, port 6655)
Connection from 184.73.10.28 port 6655 [tcp/*] accepted (family 2, sport 12345)
GET /picture-54679.jpg HTTP/1.1' or protocol-specific like 'CLIENT libcurl 7.22.0 picture-54679.jpg QUIT'.

## Related

- [[commands/curl-send-ssrf-request]]
- [[procedures/Verify-SSRF-with-Netcat-Listener]]
