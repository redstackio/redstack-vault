---
data: './src/curl --insecure -c cookies -vv -L https://$(hostname):9443'
tags:
  - curl
  - trigger
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.003Z'
id: 9e8afd3b-4040-4a2d-abd4-ad4e8e41134b
verified: false
validated: true
submitted: true
---
# curl-trigger-vuln

## Command

```bash
./src/curl --insecure -c cookies -vv -L https://$(hostname):9443
```

## Description

Executes curl to trigger OOB read by following redirect and handling cookies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --insecure | Skip SSL verify | Yes |
| -c cookies | Save cookies | Yes |
| -vv | Verbose | Yes |
| -L | Follow redirects | Yes |
| URL | HTTPS endpoint | Yes |

## Examples

### Basic Usage

```bash
./src/curl --insecure -c cookies -vv -L https://$(hostname):9443
```

## Expected Output

HTTP headers, redirect, ASan error.

## Related

- [[procedures/Execute-curl-to-Trigger-Vulnerability]]
- [[procedures/Observe-AddressSanitizer-Report]]
