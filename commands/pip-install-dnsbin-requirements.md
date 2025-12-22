---
id: 80f80b2d-4509-4893-9d64-16fcd2a8328e
name: pip-install-dnsbin-requirements
type: command
executor: bash
data: pip install -r requirements.txt
output: null
created_at: '2023-04-06T03:55:57.488699+00:00'
updated_at: '2023-04-06T03:55:57.503153+00:00'
platforms:
  - Linux
tags:
  - setup
  - dnsbin
  - python
verified: true
validated: true
---

# pip-install-dnsbin-requirements

## Command

```bash
pip install -r requirements.txt
```

## Description

Installs the Python dependencies required for running the dnsbin tool, such as DNS libraries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r requirements.txt | Install from requirements file | Yes |

## Examples

### Basic Usage

```bash
pip install -r requirements.txt
```

### With Virtual Environment

```bash
pip3 install -r requirements.txt
```

## Expected Output

Collecting dnspython>=2.0.0 (from -r requirements.txt (line 1))
  Downloading dnspython-2.4.2-py3-none-any.whl (285 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 285.7/285.7 kB 1.2 MB/s eta 0:00:00
Installing collected packages: dnspython
Successfully installed dnspython-2.4.2

## Related

- [[procedures/DNS-Data-Exfiltration-via-Command-Injection]]
- [[tools/dnsbin]]
