---
data: nc -v -l 11111
tags:
  - listener
  - tcp
type: command
output: >-
  Connection from [Imgur IP] port 11111 [tcp] accepted; e.g.,
  SSH-2.0-libssh2_1.4.2 or CLIENT libcurl 7.40.0 followed by QUIT
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:08.996Z'
id: f8caa071-ba51-46df-9c44-7daa0f157de5
verified: false
validated: true
submitted: true
---
# nc-listen-tcp-verbose

## Command

```bash
nc -v -l 11111
```

## Description

Listen for incoming TCP connections on port 11111 with verbose output to capture SSRF-triggered sessions and protocol banners from Imgur servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output showing connection details | Yes |
| `-l` | Listen mode for incoming connections | Yes |
| `11111` | Port to bind to | Yes |

## Examples

### Basic Usage

```bash
nc -v -l 11111
```

### Advanced Usage

```bash
nc -v -l -p 11111 -w 10
```

> Adds timeout (-w 10 seconds) for auto-close.

## Expected Output

Connection from [IP] port 11111 accepted, followed by protocol-specific data like SSH banners or DICT responses.

## Related

- [[commands/nc-listen-udp-verbose]]
- [[procedures/Capture-SSRF-Connections-with-Netcat-for-Info-Disclosure]]
