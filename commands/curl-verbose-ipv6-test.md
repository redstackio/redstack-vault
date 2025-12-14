---
id: 123e4567-e89b-12d3-a456-426614174003
name: curl-verbose-ipv6-test
type: command
executor: bash
data: 'curl -g ''http://[::ffff:0127.0.0.1]/'' -v -o /dev/null'
output: >-
  * URL rejected: Bad IPv6 address\n* Closing connection\ncurl: (3) URL
  rejected: Bad IPv6 address (on Linux)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:54.941Z'
platforms:
  - Linux
  - macOS
tags:
  - ssrf
  - test
verified: false
validated: true
submitted: true
---

# curl-verbose-ipv6-test

## Command

```bash
curl -g 'http://[::ffff:0127.0.0.1]/' -v -o /dev/null
```

## Description

Tests the IPv6 payload with verbose output and globbing disabled to observe platform-specific rejection or acceptance in curl parsing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -g | Disable URL globbing | Yes |
| -v | Verbose output | Yes |
| URL | http://[::ffff:0127.0.0.1]/ | Yes |
| -o /dev/null | Discard output body | Yes |

## Examples

### Basic Usage

```bash
curl -g 'http://[::ffff:0127.0.0.1]/' -v -o /dev/null
```

### Advanced Usage

```bash
curl -g 'http://[::ffff:0127.0.0.1]/' -v -o /dev/null --connect-timeout 5
```

## Expected Output

On Linux: * URL rejected: Bad IPv6 address\n* Closing connection\ncurl: (3) URL rejected: Bad IPv6 address. On macOS: May connect successfully.

## Related

- [[commands/curl-ssrf-poc-with-octal-ipv6]]
- [[procedures/Demonstrate-Curl-SSRF-with-Octal-IPv6]]
