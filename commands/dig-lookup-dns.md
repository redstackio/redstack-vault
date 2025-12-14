---
id: cmd-dig-lookup
data: dig example-sub.mozaws.net CNAME
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
updated_at: '2025-12-14T04:38:39.348Z'
verified: false
validated: true
submitted: true
---
# dig-lookup-dns

## Command

```bash
dig example-sub.mozaws.net CNAME
```

## Description

This command uses the dig utility to query DNS for a specific record type (CNAME) on a subdomain, helping identify dangling records in subdomain takeover scenarios. Use it during reconnaissance to check if a CNAME points to an existing resource.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `example-sub.mozaws.net` | The subdomain to query | Yes |
| `CNAME` | Record type to fetch (e.g., CNAME, ANY) | Yes |
| `+short` (optional) | Short output format | No |

## Examples

### Basic Usage

```bash
dig example-sub.mozaws.net CNAME
```

### Advanced Usage

```bash
dig +short example-sub.mozaws.net ANY
```

## Expected Output

DNS response with authority section showing CNAME, e.g., "example-sub.mozaws.net. 300 IN CNAME dangling-bucket.s3.amazonaws.com." If no answer or NXDOMAIN on target, it's dangling.

## Related

- [[Related Procedure: Identify-Dangling-DNS-Records]]
