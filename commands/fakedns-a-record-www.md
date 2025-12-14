---
data: A www.yourdomain.com YOUR.PUBLIC.IP
tags:
  - dns
  - a-record
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.242Z'
id: 75e97ac3-0d87-4650-87f9-fb91e118e702
verified: false
validated: true
submitted: true
---
# FakeDns A Record for WWW Subdomain

## Command

```bash
A www.yourdomain.com YOUR.PUBLIC.IP
```

## Description

Adds an A record in FakeDns configuration to map the www subdomain to the attacker's public IP, allowing the initial Bitwarden icon fetch to reach the controlled server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| A | DNS record type (IPv4 address) | Yes |
| www.yourdomain.com | Subdomain to map | Yes |
| YOUR.PUBLIC.IP | Public IP address of server | Yes |

## Examples

### Basic Usage

```bash
A www.example.com 203.0.113.1
```

### Advanced Usage

Integrate into FakeDns startup script for multiple records.

## Expected Output

DNS resolution to public IP for initial fetch; no output from command itself, but verifiable with `dig www.yourdomain.com @localhost` pointing to FakeDns.

## Related

- [[commands/fakedns-a-record-local]]
- [[procedures/Setup-FakeDns-with-Malicious-Records]]
