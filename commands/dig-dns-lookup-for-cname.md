---
data: dig cloudfront.ubnt.com
tags:
  - dns
  - reconnaissance
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:31.349Z'
id: 7be1fdb0-45be-4b10-8798-b7973c026d9d
verified: false
validated: true
submitted: true
---
# dig-dns-lookup-for-cname

## Command

```bash
dig cloudfront.ubnt.com
```

## Description

This command performs a DNS query to resolve the A record for a subdomain, revealing any CNAME records pointing to cloud services like CloudFront, useful for detecting subdomain takeover vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cloudfront.ubnt.com` | The target subdomain to query | Yes |
| `+cmd` | Global option to show command output format (optional) | No |

## Examples

### Basic Usage

```bash
dig cloudfront.ubnt.com
```

### Advanced Usage

```bash
dig +short cloudfront.ubnt.com
```

## Expected Output

Detailed DNS response including QUESTION SECTION, AUTHORITY SECTION, and ANSWER SECTION with CNAME du6drkqe7qw4g.cloudfront.net followed by multiple A records like 52.222.171.58, 52.222.176.20, etc. Query time, server, and msg id included. Indicates unclaimed if no custom origin details.

## Related

- [[Related Procedure: Detect-Dangling-CNAME-with-DNS-Lookup]]
