---
data: dig svcgatewayloadus.starbucks.com A
tags:
  - dns
  - recon
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 4f25f93d-a2fa-4d47-a272-6618eee5c694
created_at: '2025-12-14T04:51:26.610Z'
updated_at: '2025-12-14T04:51:26.610Z'
verified: false
validated: true
submitted: true
---
# dig-query-svcgatewayloadus-starbucks-com-A

## Command

```bash
dig svcgatewayloadus.starbucks.com A
```

## Description

This command performs a DNS lookup for the A record of the Starbucks load subdomain, revealing a CNAME to an unclaimed Azure Traffic Manager endpoint during vulnerability reconnaissance for subdomain takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `svcgatewayloadus.starbucks.com` | Target subdomain to query | Yes |
| `A` | Record type for IPv4 addresses (triggers CNAME revelation) | Yes |

## Examples

### Basic Usage

```bash
dig svcgatewayloadus.starbucks.com A
```

### Advanced Usage

```bash
dig +short svcgatewayloadus.starbucks.com A
```

## Expected Output

CNAME record pointing to s00197tmp0crdfulload0.trafficmanager.net followed by NXDOMAIN status, confirming the endpoint is unclaimed.

## Related

- [[commands/dig-query-svcgatewaydevus-starbucks-com-A]]
- [[procedures/Discover-Unclaimed-Subdomains-via-DNS-Query]]
