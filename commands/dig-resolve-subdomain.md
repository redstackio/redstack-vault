---
data: dig +short sales.mixmax.com
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
updated_at: '2025-12-14T05:32:23.879Z'
id: 33469c51-1990-4678-9df4-49d74e252fa5
verified: false
validated: true
submitted: true
---
# dig-resolve-subdomain

## Command

```bash
dig +short sales.mixmax.com
```

## Description

This command uses the dig utility to perform a quick DNS lookup on a subdomain, returning only the IP address for fast identification of hosting providers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `+short` | Limits output to essential records (IPs) | Yes |
| `sales.mixmax.com` | The subdomain to resolve | Yes |

## Examples

### Basic Usage

```bash
dig +short sales.mixmax.com
```

### Advanced Usage

```bash
dig sales.mixmax.com ANY
```
(For full records including CNAME)

## Expected Output

A single line with the resolved IP, e.g., '151.101.16.229', indicating the hosting endpoint.

## Related

- [[nslookup-query]]
- [[procedures/Discover-Dangling-Subdomain-DNS-Record]]
