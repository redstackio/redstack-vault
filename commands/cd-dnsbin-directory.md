---
id: 5292d3e7-e763-4502-9eee-b7556c56c161
name: cd-dnsbin-directory
type: command
executor: bash
data: cd dnsbin
output: null
created_at: '2023-04-06T03:55:57.488562+00:00'
updated_at: '2023-04-06T03:55:57.503057+00:00'
platforms:
  - Linux
tags:
  - setup
  - dnsbin
verified: true
validated: true
---

# cd-dnsbin-directory

## Command

```bash
cd dnsbin
```

## Description

Changes the current working directory to the dnsbin folder after cloning the repository, preparing for installation and execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| dnsbin | Directory name | Yes |

## Examples

### Basic Usage

```bash
cd dnsbin
```

## Expected Output

No output; use `pwd` to confirm: /path/to/dnsbin

## Related

- [[procedures/DNS-Data-Exfiltration-via-Command-Injection]]
- [[commands/git-clone-dnsbin-repo]]
