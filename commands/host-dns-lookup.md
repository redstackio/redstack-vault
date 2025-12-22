---
id: cmd-host-dns-lookup
data: host code.wordpress.net
tags:
  - dns
  - recon
type: command
output: >-
  code.wordpress.net is an alias for wpprojects.wordpress.com.
  wpprojects.wordpress.com is an alias for lb.wordpress.com. lb.wordpress.com
  has address 192.0.78.13 lb.wordpress.com has address 192.0.78.12
executor: bash
platforms:
  - Linux
  - macOS
  - Windows (with Cygwin)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:24.152Z'
verified: false
validated: true
submitted: true
---
# host-dns-lookup

## Command

```bash
host code.wordpress.net
```

## Description

The 'host' command performs DNS lookups to resolve domain names, retrieving aliases (CNAMEs) and associated IP addresses. It is used here to verify subdomain configurations and detect dangling records in takeover scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain | The target domain or subdomain to query (e.g., code.wordpress.net) | Yes |
| -t | Specify record type (e.g., -t CNAME for aliases only) | No |
| -v | Verbose output for detailed resolution steps | No |

## Examples

### Basic Usage

```bash
host code.wordpress.net
```

### Advanced Usage

```bash
host -t CNAME -v code.wordpress.net
```

## Expected Output

Successful execution shows the CNAME chain and IPs: "code.wordpress.net is an alias for wpprojects.wordpress.com. wpprojects.wordpress.com is an alias for lb.wordpress.com. lb.wordpress.com has address 192.0.78.13 lb.wordpress.com has address 192.0.78.12". Look for unclaimed service indicators in the chain.

## Related

- [[Related Procedure: Detect-and-Confirm-Subdomain-Takeover]]
