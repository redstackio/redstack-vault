---
type: command
executor: bash
data: |
  prips $_IP_RANGE | hakrevdns 
output: null
platforms:
  - Linux
tags:
  - reconnaissance
  - dns
verified: true
validated: true
---

# hakrevdns-lookup-subdomains-from-ip-range

## Command

```bash
prips $_IP_RANGE | hakrevdns
```

## Description

This command expands a CIDR IP range into individual addresses using prips and pipes them to hakrevdns for bulk reverse DNS lookups, outputting any discovered subdomains. Use it during reconnaissance to map IP blocks to hostnames efficiently.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_IP_RANGE | CIDR notation for the IP range (e.g., 173.0.84.0/24) | Yes |
| prips | Tool to print IP addresses from range (assumes installed) | Yes |
| hakrevdns | Reverse DNS tool for subdomain discovery | Yes |

## Examples

### Basic Usage

```bash
prips 173.0.84.0/24 | hakrevdns
```

### Advanced Usage

For a larger range with output redirection:

```bash
prips 10.0.0.0/16 | hakrevdns > subdomains.txt
```

## Expected Output

The command outputs lines in the format "IP_ADDRESS DOMAIN_NAME" for resolved subdomains, or just the IP if no PTR record exists. Example:

```
173.0.84.1
173.0.84.110 mail.example.com
173.0.84.111 api.example.com
```

## Related

- [[procedures/Reverse-DNS-Lookup-for-Subdomains-Using-Hakrevdns]]
- [[tools/hakrevdns]]
