---
id: cmd-curl-test-ip-with-protocol
data: 'curl -L -I "https://www.uber.com//216.58.217.206/calendar"'
tags:
  - testing
  - ip
  - redirect
type: command
output: |-
  HTTP/1.1 404 Not Found or SSL error
  ...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:26.886Z'
verified: false
validated: true
submitted: true
---
# curl-test-ip-with-protocol

## Command

```bash
curl -L -I "https://www.uber.com//216.58.217.206/calendar"
```

## Description

Probes Uber.com with IP after double slashes under HTTPS to detect errors like 404 or SSL mismatches.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow redirects | Yes |
| `-I` | Headers only | Yes |
| URL | IP-embedded URL | Yes |

## Examples

### Basic Usage

```bash
curl -L -I "https://www.uber.com//216.58.217.206/calendar"
```

### Advanced Usage

Add `-v` for verbose SSL details.

## Expected Output

404 or SSL error, blocking redirect.

## Related

- [[Related Procedure: Exploit-IP-Based-Redirect]]
