---
id: 858192fb-90ed-4978-9490-3645f2e0a611
type: command
executor: bash
data: >-
  amass enum -rf $_RESOLVERS_FILE -src -ip -d $_TARGET_DOMAIN -max-dns-queries
  $_MAX_QUERIES_NUM
output: "root@kali ~# amass enum -rf 25.txt -src -ip -d owasp.org -max-dns-queries 20000\nQuerying DNSDumpster for owasp.org subdomains\n... [various sources and discoveries] ...\nAverage DNS queries performed: 355/sec, Average retries required: 9.58%\nAverage DNS queries performed: 110/sec, Average retries required: 9.09%\n[Alterations]     6ntact.owasp.org 180.122.78.238,180.122.78.239,180.122.78.240,180.122.78.243,180.122.78.242,180.122.78.248,180.122.78.244,180.122.78.241\n[Alterations]     gvirt-host.owasp.org 163.171.139.156\n\nOWASP Amass v3.7.2                                https://github.com/OWASP/Amass\n--------------------------------------------------------------------------------\n19 names discovered - cert: 9, api: 8, alt: 2\n--------------------------------------------------------------------------------\nASN: 13335 - CLOUDFLARENET, US\n\t104.22.16.0/20    \t32   Subdomain Name(s)\n\t172.67.0.0/20     \t16   Subdomain Name(s)\n\t2606:4700::/32    \t21   Subdomain Name(s)\nASN: 4134 - CHINANET-BACKBONE No.31,Jin-rong Street, CN\n\t180.96.0.0/11     \t8    Subdomain Name(s)\nASN: 54994 - QUANTILNETWORKS, US\n\t163.171.139.0/24  \t1    Subdomain Name(s)\n\nThe enumeration has finished\nDiscoveries are being migrated into the Cayley Graph database"
created_at: '2020-06-30T03:02:02.411205+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - subdomain
  - custom-resolvers
verified: true
validated: true
---

# amass-enumerate-subdomains-with-custom-resolvers

## Command

```bash
amass enum -rf $_RESOLVERS_FILE -src -ip -d $_TARGET_DOMAIN -max-dns-queries $_MAX_QUERIES_NUM
```

## Description

Advanced subdomain enumeration using custom resolvers, passive sources, IP resolution, and query limits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -rf $_RESOLVERS_FILE | Custom resolvers file | Yes |
| -src | Passive sources only | Yes |
| -ip | Resolve IPs | Yes |
| -d $_TARGET_DOMAIN | Target domain | Yes |
| -max-dns-queries $_MAX_QUERIES_NUM | Max queries per source | Yes |

## Examples

### Basic Usage

```bash
amass enum -rf resolvers.txt -src -ip -d example.com -max-dns-queries 20000
```

## Expected Output

Detailed discoveries from sources, with subdomains, IPs, and ASN summaries.

## Related

- [[procedures/Enumerate-Subdomains-with-Amass]]
- [[tools/amass]]
