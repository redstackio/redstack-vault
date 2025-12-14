---
id: cmd-001
data: dig A ████
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
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.319Z'
verified: false
validated: true
submitted: true
---
# dig-dns-lookup-for-origin-ip

## Command

```bash
dig A ████
```

## Description

This command performs a DNS A record lookup for the target domain to trace the CNAME chain and identify the origin IP behind Akamai load balancer. Use it during reconnaissance to map CDN-protected infrastructure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| A | Query type for IPv4 addresses | Yes |
| ████ | Target domain name | Yes |

## Examples

### Basic Usage

```bash
dig A ████
```

### Advanced Usage

```bash
dig +trace A ████
```

> Adds tracing for full delegation path.

## Expected Output

ANSWER SECTION with CNAMEs like ███. 2386 IN CNAME █████. and A record for Akamai edge server, helping identify backend IPs.

## Related

- [[Related Procedure]]: [[procedures/DNS-Lookup-to-Identify-Origin-IP-Behind-Akamai]]
