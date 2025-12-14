---
data: dig +short dev-admin.periscope.tv
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
updated_at: '2025-12-14T04:38:39.732Z'
id: c5d66653-2235-4772-af27-dd325f9dd217
verified: false
validated: true
submitted: true
---
# dig-check-dns

## Command

```bash
dig +short dev-admin.periscope.tv
```

## Description

This command performs a concise DNS lookup to retrieve the IP or CNAME for a subdomain, useful for identifying resolutions to cloud endpoints like AWS S3.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `+short` | Outputs only the resolved record without verbose details | Yes |
| `dev-admin.periscope.tv` | The subdomain to query | Yes |

## Examples

### Basic Usage

```bash
dig +short dev-admin.periscope.tv
```

### Advanced Usage

```bash
dig +short @8.8.8.8 dev-admin.periscope.tv CNAME
```

## Expected Output

A single line with the resolved hostname, e.g., "dev-admin.periscope.tv.s3-website-us-west-2.amazonaws.com."

## Related

- [[Related Procedure|procedures/Discover-Dangling-Subdomain-for-Takeover]]
