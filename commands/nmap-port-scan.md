---
id: cmd-nmap-port
data: nmap -p 443 auth.zomato.com
tags:
  - port-scan
type: command
output: 443/tcp open https
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:32.223Z'
verified: false
validated: true
submitted: true
---
# nmap-port-scan

## Command

```bash
nmap -p 443 auth.zomato.com
```

## Description

Scans specific port on subdomain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p | Port to scan | Yes |
| host | Target host | Yes |

## Examples

### Basic Usage

```bash
nmap -p 443 auth.zomato.com
```

## Expected Output

Port status open/closed.

## Related

- [[commands/nmap-host-scan]]
