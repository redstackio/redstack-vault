---
id: cmd-dig-query
data: dig +short CNAME suspected-subdomain.mozaws.net
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
updated_at: '2025-12-14T05:32:23.337Z'
verified: false
validated: true
submitted: true
---
# dig-query

## Command

```bash
dig +short CNAME suspected-subdomain.mozaws.net
```

## Description

This command uses the dig utility to perform a quick DNS query for the CNAME record of a specified subdomain, useful for identifying dangling records in takeover scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `+short` | Outputs only the relevant record without verbose details | Yes |
| `CNAME` | Specifies the query type for canonical name records | Yes |
| `suspected-subdomain.mozaws.net` | The target subdomain to query | Yes |

## Examples

### Basic Usage

```bash
dig +short CNAME example-sub.mozaws.net
```

### Advanced Usage

```bash
dig +short @8.8.8.8 CNAME example-sub.mozaws.net
```

(Uses Google's DNS server for resolution.)

## Expected Output

A single line with the CNAME target, e.g., "unregistered-domain.com". If no CNAME, empty or error.

## Related

- [[Related Procedure: Discover Dangling DNS Records]]
