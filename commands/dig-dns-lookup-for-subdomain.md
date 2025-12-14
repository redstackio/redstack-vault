---
data: dig www.███████
tags:
  - dns
  - recon
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: caba1b19-7914-4fc4-beb4-548a07460c2b
created_at: '2025-12-14T05:32:31.164Z'
updated_at: '2025-12-14T05:32:31.164Z'
verified: false
validated: true
submitted: true
---
# dig DNS Lookup for Subdomain

## Command

```bash
dig www.███████
```

## Description

This command uses the dig utility to perform a DNS lookup on a target subdomain, revealing records like CNAMEs that may point to unclaimed cloud resources, aiding in subdomain takeover detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `www.███████` | The target subdomain to query for DNS resolution | Yes |

## Examples

### Basic Usage

```bash
dig www.███████
```

### Advanced Usage

```bash
dig +short www.███████ CNAME
```

> Limits output to CNAME records only.

## Expected Output

DNS resolution showing CNAME to unclaimed bucket (e.g., "www.███████. 300 IN CNAME bucket.s3.amazonaws.com"), NS records for name servers, and A records. Indicates vulnerability if CNAME targets an available S3 endpoint.

## Related

- [[Related Procedure: DNS-Enumeration-for-Subdomain-Takeover]]
