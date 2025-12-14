---
id: cmd-nmap-service-927413
data: nmap -p 443 -sV auth.zomato.com
tags:
  - scanning
type: command
output: |
  PORT    STATE SERVICE VERSION
  443/tcp open  https (misconfig possible)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.603Z'
verified: false
validated: true
submitted: true
---
# nmap-service-scan

## Command

```bash
nmap -p 443 -sV auth.zomato.com
```

## Description

Scans specific port on auth subdomain for service details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p 443` | Target port | Yes |
| `-sV` | Version detection | No |
| `auth.zomato.com` | Target | Yes |

## Examples

### Basic Usage

```bash
nmap -p 443 target.com
```

### Advanced Usage

```bash
nmap -p 443 -A target.com
```

## Expected Output

Service on 443 confirmed, potential misconfig.

## Related

- [[Related Procedure: Exposed-Service-Detection-on-Auth-Domain]]
