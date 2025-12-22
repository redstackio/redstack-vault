---
id: 61ea9a8d-1bcb-4a28-95c6-a028a5e7e578
name: python-start-dnsbin-server
type: command
executor: bash
data: python dnsbin.py
output: null
created_at: '2023-04-06T03:55:57.488766+00:00'
updated_at: '2023-04-06T03:55:57.503168+00:00'
platforms:
  - Linux
tags:
  - setup
  - dnsbin
  - server
verified: true
validated: true
---

# python-start-dnsbin-server

## Command

```bash
python dnsbin.py
```

## Description

Starts the dnsbin DNS server, which listens for queries and provides a unique subdomain for exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| dnsbin.py | Main script | Yes |

## Examples

### Basic Usage

```bash
python dnsbin.py
```

### With Python 3

```bash
python3 dnsbin.py
```

## Expected Output

Your DNS bin is: abc123def456.dnsbin.zhack.ca
Server listening on 0.0.0.0:53

## Related

- [[procedures/DNS-Data-Exfiltration-via-Command-Injection]]
- [[tools/dnsbin]]
