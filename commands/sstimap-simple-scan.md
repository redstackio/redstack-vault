---
id: c3d98972-83ec-4eb3-9bf9-9aba2b74df0e
name: sstimap-simple-scan
type: command
executor: bash
data: 'python3 ./sstimap.py -u ''https://example.com/page?name=John'' -s'
output: null
created_at: '2023-04-06T03:56:38.834404+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - ssti
  - detection
verified: true
validated: true
---

# sstimap-simple-scan

## Command

```bash
python3 ./sstimap.py -u 'https://example.com/page?name=John' -s
```

## Description

This command performs a basic scan for Server-Side Template Injection (SSTI) vulnerabilities on a target URL using sstimap. It probes parameters for template payload execution without advanced options, ideal for initial reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Target URL with potential injection points | Yes |
| -s | Perform simple scan mode | Yes |

## Examples

### Basic Usage

```bash
python3 ./sstimap.py -u 'https://example.com/page?name=John' -s
```

### Advanced Usage

Add more parameters if needed, but keep simple for initial tests.

## Expected Output

If vulnerable, output will show detected template engines and payload success, e.g.,:
```
[+] SSTI detected in parameter 'name' using Jinja2 engine.
[*] Payload executed: {{7*7}} -> 49
```
No output or errors indicate no vulnerability.

## Related

- [[procedures/Exploit-Server-Side-Template-Injection-with-tplmap-and-sstimap]]
- [[tools/sstimap]]
