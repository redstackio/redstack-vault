---
data: dig blog.gnipcentral.com
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
id: 3155c2df-c925-4ea5-8508-b11cacbfb850
created_at: '2025-12-14T04:51:26.412Z'
updated_at: '2025-12-14T04:51:26.412Z'
verified: false
validated: true
submitted: true
---
# dig-check-cname

## Command

```bash
dig blog.gnipcentral.com
```

## Description

This command uses the dig utility to query DNS records for a subdomain, specifically checking for CNAME entries that may indicate dangling records pointing to cloud services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `blog.gnipcentral.com` | The target subdomain to query | Yes |

## Examples

### Basic Usage

```bash
dig blog.gnipcentral.com
```

### Advanced Usage

```bash
dig +short CNAME blog.gnipcentral.com
```

## Expected Output

DNS response including ANSWER SECTION with CNAME record, e.g., blog.gnipcentral.com. 300 IN CNAME testcloudfrontbug.s3-us-west-2.amazonaws.com.

## Related

- [[Related Procedure: Discover-Dangling-Subdomain-CNAME]]
