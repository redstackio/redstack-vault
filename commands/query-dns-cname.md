---
data: dig $SUBDOMAIN CNAME
tags:
  - dns
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.451Z'
id: bd54aef0-a962-42f7-8a4d-dbd321904f78
verified: false
validated: true
submitted: true
---
# query-dns-cname

## Command

```bash
dig $SUBDOMAIN CNAME
```

## Description

This command uses the dig utility to query DNS for the CNAME record of a specified subdomain, helping identify if it points to a third-party service for potential dangling record detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$SUBDOMAIN` | The target subdomain to query (e.g., support.scan.me) | Yes |

## Examples

### Basic Usage

```bash
dig support.scan.me CNAME
```

### Advanced Usage

```bash
dig +short support.scan.me CNAME
```

## Expected Output

DNS response with CNAME details, e.g., "support.scan.me. 3600 IN CNAME scan.zendesk.com." indicating a potential dangling record if the target is unused.

## Related

- [[Related Procedure|procedures/Discover-Dangling-CNAME-Records]]
