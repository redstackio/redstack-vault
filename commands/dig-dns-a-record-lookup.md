---
data: dig A a2.bime.io @8.8.8.8
tags:
  - dns
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.371Z'
id: a70453db-93ce-4bb4-8974-26c7a790b59f
verified: false
validated: true
submitted: true
---
# dig-dns-a-record-lookup

## Command

```bash
dig A a2.bime.io @8.8.8.8
```

## Description

Performs a DNS A record lookup for a subdomain using a specified resolver to identify backend services like AWS S3 in takeover scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `A` | Query type for IPv4 address | Yes |
| `domain` | Target subdomain (e.g., a2.bime.io) | Yes |
| `@8.8.8.8` | DNS server (Google public resolver) | No (default system) |

## Examples

### Basic Usage

```bash
dig A example.com
```

### Advanced Usage

```bash
dig A a2.bime.io @8.8.8.8 +short
```

## Expected Output

Detailed DNS response including authority section with CNAME to s3-website-us-east-1.amazonaws.com and A record 54.231.11.130.

## Related

- [[Related Procedure: Resolve-DNS-for-Subdomain-Takeover-Detection]]
