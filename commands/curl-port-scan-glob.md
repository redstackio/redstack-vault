---
data: 'curl -vv ''http://1.1.1.1:[80-9000]/'''
tags:
  - port-scanning
type: command
output: >-
  Multiple connection attempts; successes for open ports, errors/timeouts for
  closed ones, enabling port scanning
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.302Z'
id: 9048a450-0ae6-4ea0-b1d2-099c4b6c6d81
verified: false
validated: true
submitted: true
---
# curl-port-scan-glob

## Command

```bash
curl -vv 'http://1.1.1.1:[80-9000]/'
```

## Description

Uses curl to glob a port range for scanning open services on a target host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-vv` | Verbose output | Yes |
| `URL` | 'http://1.1.1.1:[80-9000]/' with port glob | Yes |

## Examples

### Basic Usage

```bash
curl -vv 'http://1.1.1.1:[80-9000]/'
```

### Advanced Usage

```bash
curl -vv --max-time 5 'http://1.1.1.1:[80-9000]/'
```

## Expected Output

Multiple connection attempts; successes for open ports, errors/timeouts for closed ones, enabling port scanning

## Related

- [[Related Procedure]]
