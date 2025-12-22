---
id: cmd-uuid-2
data: dig +short subdomain.example.com
tags:
  - dns
  - query
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:31.220Z'
verified: false
validated: true
submitted: true
---
# dig-lookup-subdomain

## Command

```bash
dig +short subdomain.example.com
```

## Description

This command performs a quick DNS lookup using dig to resolve a subdomain, revealing CNAMEs or IPs that may indicate dangling records pointing to terminated resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `+short` | Minimal output format | No |
| `subdomain.example.com` | Target to query | Yes |

## Examples

### Basic Usage

```bash
dig +short █.staging.█.8x8.com
```

### Advanced Usage

```bash
dig +trace █.staging.█.8x8.com
```

## Expected Output

Short response like a CNAME to an EC2 alias, e.g., ec2-xxx.us-east-1.compute.amazonaws.com.

## Related

- [[Related Procedure: Verify DNS Misconfiguration for AWS Subdomain Takeover]]
