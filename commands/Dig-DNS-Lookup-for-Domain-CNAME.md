---
id: cmd-dig-cname-summit
data: dig summit.acronis.events
tags:
  - dns
  - recon
  - cname
type: command
output: |-
  summit.acronis.events. 119 IN CNAME sslevents.bizzabo.com.
  sslevents.bizzabo.com. 59 IN A 3.209.192.154
  sslevents.bizzabo.com. 59 IN A 34.192.127.27
  sslevents.bizzabo.com. 59 IN A 52.72.168.6
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.494Z'
verified: false
validated: true
submitted: true
---
# Dig-DNS-Lookup-for-Domain-CNAME

## Command

```bash
dig summit.acronis.events
```

## Description

This dig command performs a DNS lookup on the target domain to resolve CNAME and A records, useful for verifying third-party hosting in vulnerability assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `summit.acronis.events` | Domain to query | Yes |

## Examples

### Basic Usage

```bash
dig example.com
```

### Advanced Usage

```bash
dig +short summit.acronis.events CNAME
```

## Expected Output

DNS records showing CNAME to sslevents.bizzabo.com and associated A records pointing to AWS IPs.

## Related

- [[Related Procedure: Exploit-SSRF-via-bzIframeUrl-to-AWS-Metadata]]
