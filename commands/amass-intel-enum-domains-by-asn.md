---
id: ed440e9d-f373-4cee-abfd-dbb36948de91
type: command
executor: bash
data: amass intel -asn $_ASN
output: |
  root@kali ~# amass intel -asn 41264
  corp.google.com
created_at: '2020-06-29T16:38:40.327469+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - amass
  - osint
verified: true
validated: true
---

# amass-intel-enum-domains-by-asn

## Command

```bash
amass intel -asn $_ASN
```

## Description

This command uses Amass's intel subcommand to enumerate domains associated with a given Autonomous System Number (ASN) by querying passive public sources such as BGP data, certificate transparency logs, and WHOIS records. It helps map an organization's domain footprint during reconnaissance without active network interaction, making it suitable for stealthy OSINT gathering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ASN | The target ASN (e.g., 41264 for a specific organization) | Yes |
| -asn | Flag to trigger ASN-based enumeration | Built-in |
| -o | Optional output file to save results | No |

## Examples

### Basic Usage

```bash
amass intel -asn 41264
```

### Advanced Usage

```bash
amass intel -asn 41264 -o domains.txt
```

This redirects the domain list to a file.

## Expected Output

```
root@kali ~# amass intel -asn 41264
corp.google.com
```

A list of domains associated with the ASN, one per line. Empty output indicates no domains found or limited source data.

## Related

- [[tools/amass]]
- [[commands/amass-enum-passive-domain]]
