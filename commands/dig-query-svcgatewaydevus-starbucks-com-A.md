---
data: dig svcgatewaydevus.starbucks.com A
tags:
  - dns
  - recon
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 5bd46642-8cc3-4f44-bf57-7c9c3d82b683
created_at: '2025-12-14T04:51:26.609Z'
updated_at: '2025-12-14T04:51:26.609Z'
verified: false
validated: true
submitted: true
---
# dig-query-svcgatewaydevus-starbucks-com-A

## Command

```bash
dig svcgatewaydevus.starbucks.com A
```

## Description

This command queries the DNS A record for the Starbucks dev subdomain, exposing a CNAME to an unclaimed Azure Traffic Manager endpoint as part of subdomain takeover discovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `svcgatewaydevus.starbucks.com` | Target subdomain to query | Yes |
| `A` | Record type for IPv4 addresses | Yes |

## Examples

### Basic Usage

```bash
dig svcgatewaydevus.starbucks.com A
```

### Advanced Usage

```bash
dig +short svcgatewaydevus.starbucks.com A
```

## Expected Output

CNAME to s00197tmp0crdfuldev0.trafficmanager.net with NXDOMAIN, indicating availability for claiming.

## Related

- [[commands/dig-query-svcgatewayloadus-starbucks-com-A]]
- [[procedures/Discover-Unclaimed-Subdomains-via-DNS-Query]]
