---
id: 5686dde6-76d6-4990-8925-b470806c8c28
name: sstimap-jade-template-scan
type: command
executor: bash
data: >-
  python3 ./sstimap.py -u
  'https://example.com/page?name=Vulnerable*&message=My_message' -l 5 -e jade
output: null
created_at: '2023-04-06T03:56:38.834500+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - ssti
  - jade
verified: true
validated: true
---

# sstimap-jade-template-scan

## Command

```bash
python3 ./sstimap.py -u 'https://example.com/page?name=Vulnerable*&message=My_message' -l 5 -e jade
```

## Description

Scans for SSTI in Jade template engine with level 5 complexity, using '*' to mark injection points in URL parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Target URL with injection points marked by '*' | Yes |
| -l 5 | Scan level for obfuscated payloads | Yes |
| -e jade | Specify Jade template engine | Yes |

## Examples

### Basic Usage

```bash
python3 ./sstimap.py -u 'https://example.com/page?name=Vulnerable*&message=My_message' -l 5 -e jade
```

## Expected Output

Vulnerability confirmation like:
```
[+] Jade engine detected and vulnerable at level 5.
[*] Successful injection in 'name' parameter.
```

## Related

- [[procedures/Exploit-Server-Side-Template-Injection-with-tplmap-and-sstimap]]
- [[tools/sstimap]]
