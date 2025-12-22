---
id: 68062206-f4ac-46ca-ac49-d31ff24adef7
name: amass-intel-enumerate-domains-and-ips-by-asn
type: command
executor: bash
data: amass intel -active -asn $_ASN -ip
output: |-
  root@kali ~# amass intel -active -asn 41264 -ip
  corp.google.com 104.132.31.80
created_at: '2020-06-29T16:54:21.625706+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - amass
verified: true
validated: true
---

# amass-intel-enumerate-domains-and-ips-by-asn

## Command

```bash
amass intel -active -asn $_ASN -ip
```

## Description

This command actively enumerates domains by ASN and resolves their IP addresses using DNS queries. It builds on passive intel but adds resolution for direct network targeting, useful when IPs are needed for scanning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ASN | The target Autonomous System Number | Yes |
| -active | Enables active DNS resolution during enumeration | Built-in |
| -ip | Includes IP addresses in the output alongside domains | Built-in |

## Examples

### Basic Usage

```bash
amass intel -active -asn 41264 -ip
```

### Advanced Usage

```bash
amass intel -active -asn 41264 -ip -o domains-ips.txt
```

## Expected Output

```
root@kali ~# amass intel -active -asn 41264 -ip
corp.google.com 104.132.31.80
```

Domains paired with IPs, one per line.

## Related

- [[Related Procedure: Enumerate-Domains-by-ASN-Using-Amass]]
- [[commands/amass-intel-enumerate-domains-by-asn]]
