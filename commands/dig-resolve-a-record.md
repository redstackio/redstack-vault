---
id: cmd-uuid-001
data: dig example.com A +short
tags:
  - dns
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.921Z'
verified: false
validated: true
submitted: true
---
# dig-resolve-a-record

## Command

```bash
dig mta1a1.spmail.uber.com A +short
```

## Description

Resolves the IPv4 A record for a domain or subdomain, outputting only the IP address. Used to identify dangling IPs in subdomain takeover scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain | Target domain/subdomain | Yes |
| A | Query type for IPv4 | Yes |
| +short | Minimal output (IP only) | No |

## Examples

### Basic Usage

```bash
dig mta1a1.spmail.uber.com A +short
```

### Advanced Usage

```bash
dig @8.8.8.8 mta1a1.spmail.uber.com A +short
```

## Expected Output

Single line with IP, e.g., "52.XX.XX.XX".

## Related

- [[Related Procedure: Resolve-DNS-Record-for-Subdomain]]
